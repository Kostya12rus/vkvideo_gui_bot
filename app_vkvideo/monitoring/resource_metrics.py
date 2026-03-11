import os
import threading
import time
import tracemalloc
from typing import Any

try:
    import psutil
except ImportError:
    psutil = None


class UptimeMetricsMixin:
    def _init_uptime_metrics(self: Any) -> None:
        self._time_start = time.time()
        self.register_collector(self._collect_uptime_metrics)

    def _collect_uptime_metrics(self: Any) -> None:
        self.set_gauge("vkbot_uptime_seconds", time.time() - self._time_start)


class OpenPortMetricsMixin:
    def _init_openport_metrics(self: Any) -> None:
        self.register_collector(self._collect_openport_metrics)

    def _collect_openport_metrics(self: Any) -> None:
        if psutil is None:
            return
        process = psutil.Process(os.getpid())
        connections = process.net_connections()
        self.set_gauge("vkapp_connections", float(len(connections)))


class ThreadMetricsMixin:
    def _init_thread_metrics(self: Any) -> None:
        self.register_collector(self._collect_thread_metrics)

    def _collect_thread_metrics(self: Any) -> None:
        self.set_gauge("vkapp_thread_used", float(threading.active_count()))


class MemoryMetricsMixin:
    def _init_memory_metrics(self: Any) -> None:
        if not tracemalloc.is_tracing():
            tracemalloc.start()
        self._memory_max = 0
        self.register_collector(self._collect_memory_metrics)

    def _collect_memory_metrics(self: Any) -> None:
        if psutil is not None:
            memory_used = int(psutil.Process(os.getpid()).memory_info().rss)
            self._memory_max = max(self._memory_max, memory_used)
        else:
            current, peak = tracemalloc.get_traced_memory()
            memory_used = int(current)
            self._memory_max = max(self._memory_max, int(peak))

        self.set_gauge("vkapp_memory_used_bytes", float(memory_used))
        self.set_gauge("vkapp_memory_used_max_bytes", float(self._memory_max))


class CpuMetricsMixin:
    def _init_cpu_metrics(self: Any) -> None:
        self._cpu_max = 0.0
        self._last_wall = time.perf_counter()
        self._last_cpu = time.process_time()
        if psutil is not None:
            psutil.Process(os.getpid()).cpu_percent(interval=None)
        self.register_collector(self._collect_cpu_metrics)

    def _collect_cpu_metrics(self: Any) -> None:
        if psutil is not None:
            cpu_current = float(psutil.Process(os.getpid()).cpu_percent(interval=None))
        else:
            now_wall = time.perf_counter()
            now_cpu = time.process_time()
            wall_delta = max(now_wall - self._last_wall, 1e-6)
            cpu_delta = max(now_cpu - self._last_cpu, 0.0)
            self._last_wall = now_wall
            self._last_cpu = now_cpu
            cores = max(os.cpu_count() or 1, 1)
            cpu_current = (cpu_delta / wall_delta) * 100.0 / cores

        cpu_current = max(0.0, min(cpu_current, 100.0))
        self._cpu_max = max(self._cpu_max, cpu_current)

        self.set_gauge("vkapp_cpu_used_current", cpu_current)
        self.set_gauge("vkapp_cpu_used", self._cpu_max)
