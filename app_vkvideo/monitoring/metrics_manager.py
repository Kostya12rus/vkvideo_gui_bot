import atexit
import json
import os
import signal
import socket
import threading
import uuid
from pathlib import Path
from typing import Any, Callable

from prometheus_client import CollectorRegistry, Counter, Gauge, delete_from_gateway, push_to_gateway

from .resource_metrics import CpuMetricsMixin, MemoryMetricsMixin, OpenPortMetricsMixin, ThreadMetricsMixin, UptimeMetricsMixin


class BaseMetricsManager:
    _instances: dict[type, "BaseMetricsManager"] = {}
    _singleton_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        instance = cls._instances.get(cls)
        if instance is None:
            with cls._singleton_lock:
                instance = cls._instances.get(cls)
                if instance is None:
                    instance = super().__new__(cls)
                    cls._instances[cls] = instance
        return instance

    def __init__(
        self,
        host: str,
        port: int,
        user_id: str,
        hostname: str | None = None,
        job_name: str = "python_app",
        timeout_seconds: float = 1.5,
        config_path: str | Path | None = None,
    ) -> None:
        if getattr(self, "_initialized", False):
            return

        self.host = host
        self.port = int(port)
        self.job_name = job_name
        self.timeout_seconds = timeout_seconds
        self.pushgateway_url = f"http://{self.host}:{self.port}"

        self.registry = CollectorRegistry()
        self.config = self._load_config(config_path)
        self.default_labels = list(self.config.get("default_labels", ["user_id", "hostname"]))

        self.base_labels = {
            "user_id": str(user_id),
            "hostname": str(hostname or socket.gethostname()),
        }
        self.grouping_key = dict(self.base_labels)

        self.metrics: dict[str, Any] = {}
        self.metric_defs: dict[str, dict[str, Any]] = self.config.get("metrics", {})
        self._build_metrics()

        self._collectors: list[Callable[[], None]] = []
        self._collector_thread: threading.Thread | None = None
        self._stop_event = threading.Event()
        self._push_lock = threading.Lock()
        self._dirty = False
        self.connected = None

        self._register_shutdown_hooks()
        self.check_connection()
        self.reset_on_start()

        self._initialized = True

    @staticmethod
    def _load_config(config_path: str | Path | None) -> dict[str, Any]:
        path = Path(config_path) if config_path else Path(__file__).with_name("prs_metrics.json")
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)

    def _build_metrics(self) -> None:
        for metric_name, metric_info in self.metric_defs.items():
            metric_type = metric_info["type"].lower()
            doc = metric_info.get("documentation", metric_name)
            label_names = self.default_labels + metric_info.get("additional_labels", [])

            if metric_type == "counter":
                self.metrics[metric_name] = Counter(metric_name, doc, label_names, registry=self.registry)
            elif metric_type == "gauge":
                self.metrics[metric_name] = Gauge(metric_name, doc, label_names, registry=self.registry)
            else:
                raise ValueError(f"Unsupported metric type '{metric_type}' for '{metric_name}'")

    def _register_shutdown_hooks(self) -> None:
        atexit.register(self.shutdown)
        for sig in (signal.SIGINT, signal.SIGTERM):
            try:
                signal.signal(sig, self._handle_exit_signal)
            except Exception:  # noqa
                continue

    def _handle_exit_signal(self, signum, frame) -> None:  # noqa
        self.shutdown()
        raise SystemExit(0)

    def check_connection(self) -> bool:
        if self.connected is not None:
            return self.connected
        try:
            with socket.create_connection((self.host, self.port), timeout=self.timeout_seconds):
                self.connected = True
                return True
        except OSError:
            self.connected = False
            return False

    def reset_on_start(self) -> bool:
        if not self.check_connection():
            return False

        try:
            delete_from_gateway(self.pushgateway_url, job=self.job_name, grouping_key=self.grouping_key)
        except Exception:  # noqa
            pass

        for metric_name, metric_info in self.metric_defs.items():
            if metric_info.get("type", "").lower() != "gauge":
                continue
            if metric_info.get("additional_labels"):
                continue
            labels = self._labels_for(metric_name)
            self.metrics[metric_name].labels(**labels).set(0)

        if "vkapp_client_up" in self.metrics:
            self.metrics["vkapp_client_up"].labels(**self._labels_for("vkapp_client_up")).set(1)

        self._dirty = True
        return self._push_registry(force=True)

    def register_collector(self, collector: Callable[[], None]) -> None:
        self._collectors.append(collector)

    def start_collecting(self, collect_interval: float = 5.0) -> bool:
        if self._collector_thread and self._collector_thread.is_alive():
            return True
        if not self.check_connection():
            return False

        self.collect_interval = max(1.0, float(collect_interval))
        self._stop_event.clear()
        self._collector_thread = threading.Thread(
            target=self._collect_loop,
            name=f"{self.__class__.__name__}Collector",
            daemon=True,
        )
        self._collector_thread.start()
        return True

    def stop_collecting(self, timeout: float = 2.0) -> None:
        self._stop_event.set()
        if self._collector_thread and self._collector_thread.is_alive():
            self._collector_thread.join(timeout=timeout)

    def _collect_loop(self) -> None:
        while not self._stop_event.is_set():
            for collector in self._collectors:
                collector()
            self._push_registry(force=False)
            self._stop_event.wait(getattr(self, "collect_interval", 5.0))

    def _push_registry(self, force: bool = False) -> bool:
        if not force and not self._dirty:
            return True
        if not self.check_connection():
            return False

        with self._push_lock:
            try:
                push_to_gateway(
                    self.pushgateway_url,
                    job=self.job_name,
                    registry=self.registry,
                    grouping_key=self.grouping_key,
                )
                self._dirty = False
                return True
            except Exception:  # noqa
                return False

    def _labels_for(self, metric_name: str, extra_labels: dict[str, Any] | None = None) -> dict[str, Any]:
        metric_info = self.metric_defs[metric_name]
        labels = dict(self.base_labels)
        extra_labels = extra_labels or {}

        for label_name in metric_info.get("additional_labels", []):
            label_value = extra_labels.get(label_name)
            if label_value is None:
                label_value = "unknown"
            labels[label_name] = str(label_value)

        return labels

    def set_gauge(self, metric_name: str, value: float, **labels: Any) -> bool:
        metric_info = self.metric_defs.get(metric_name)
        if metric_info is None or metric_info.get("type", "").lower() != "gauge":
            return False

        metric_labels = self._labels_for(metric_name, labels)
        self.metrics[metric_name].labels(**metric_labels).set(value)
        self._dirty = True
        return True

    def inc_metric(self, metric_name: str, amount: float = 1.0, **labels: Any) -> bool:
        metric_info = self.metric_defs.get(metric_name)
        if metric_info is None:
            return False
        if metric_info.get("type", "").lower() != "counter":
            return False
        if amount < 0:
            return False

        metric_labels = self._labels_for(metric_name, labels)
        metric = self.metrics[metric_name].labels(**metric_labels)
        metric.inc(amount)
        self._dirty = True
        return True

    def push_now(self) -> bool:
        return self._push_registry(force=True)

    def shutdown(self) -> None:
        if getattr(self, "_shutdown_done", False):
            return
        self._shutdown_done = True

        self.stop_collecting()
        if not self.check_connection():
            return

        for metric_name in ("vkapp_client_up", "vkapp_wss_active"):
            if metric_name in self.metrics:
                self.metrics[metric_name].labels(**self._labels_for(metric_name)).set(0)
                self._dirty = True

        self._push_registry(force=True)

        try:
            delete_from_gateway(self.pushgateway_url, job=self.job_name, grouping_key=self.grouping_key)
        except Exception:  # noqa
            pass


class MetricsManager(
    ThreadMetricsMixin,
    MemoryMetricsMixin,
    CpuMetricsMixin,
    BaseMetricsManager,
    UptimeMetricsMixin,
    OpenPortMetricsMixin,
):
    def __init__(
        self,
        host: str,
        port: int,
        user_id: str,
        hostname: str | None = None,
        job_name: str = "python_app",
        timeout_seconds: float = 1.5,
        config_path: str | Path | None = None,
        collect_interval: float = 5.0,
        autostart: bool = True,
    ) -> None:
        super().__init__(
            host=host,
            port=port,
            user_id=user_id,
            hostname=hostname,
            job_name=job_name,
            timeout_seconds=timeout_seconds,
            config_path=config_path,
        )

        if getattr(self, "_resource_mixins_initialized", False):
            if autostart and self.connected:
                self.start_collecting(collect_interval=collect_interval)
            return

        self._init_uptime_metrics()
        self._init_openport_metrics()
        self._init_thread_metrics()
        self._init_memory_metrics()
        self._init_cpu_metrics()
        self._resource_mixins_initialized = True

        if autostart and self.connected:
            self.start_collecting(collect_interval=collect_interval)
