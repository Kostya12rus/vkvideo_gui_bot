import os
import threading
import time
from typing import Any

import psutil


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
        children = process.children(recursive=True)
        connections = len(process.net_connections()) + sum([len(p.net_connections()) for p in children])
        self.set_gauge("vkapp_connections", float(connections))


class ThreadMetricsMixin:
    def _init_thread_metrics(self: Any) -> None:
        self.register_collector(self._collect_thread_metrics)

    def _collect_thread_metrics(self: Any) -> None:
        self.set_gauge("vkapp_thread_used", float(threading.active_count()))


class MemoryMetricsMixin:
    def _init_memory_metrics(self: Any) -> None:
        self._memory_max = 0
        self.register_collector(self._collect_memory_metrics)

    def _collect_memory_metrics(self: Any) -> None:
        process = psutil.Process(os.getpid())
        process_memory = int(process.memory_info().rss)
        children = process.children(recursive=True)
        children_memory = sum([int(p.memory_info().rss) for p in children])

        memory_used = process_memory + children_memory
        self._memory_max = max(self._memory_max, memory_used)

        self.set_gauge("vkapp_memory_used_bytes", float(memory_used))
        self.set_gauge("vkapp_memory_used_max_bytes", float(self._memory_max))


class CpuMetricsMixin:
    def _init_cpu_metrics(self: Any) -> None:
        self._cpu_max = 0.0
        self._last_wall = time.perf_counter()
        self._last_cpu = time.process_time()
        psutil.Process(os.getpid()).cpu_percent(interval=None)
        self.register_collector(self._collect_cpu_metrics)

    def _collect_cpu_metrics(self: Any) -> None:
        cpu_current = float(psutil.Process(os.getpid()).cpu_percent(interval=None))

        cpu_current = max(0.0, min(cpu_current, 100.0))
        self._cpu_max = max(self._cpu_max, cpu_current)

        self.set_gauge("vkapp_cpu_used_current", cpu_current)
        self.set_gauge("vkapp_cpu_used", self._cpu_max)
