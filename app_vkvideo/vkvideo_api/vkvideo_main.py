import threading
import weakref
from typing import Any

from app_vkvideo.monitoring import MetricsManager
from .api import UserApi, StreamerApi, StreamersApi, WatchStreamMonitor
from .auth import AuthModule
from .heartbeat import HeartbeatApi
from .web_socket import WebSocketManager


class VKVideoApi(UserApi, StreamerApi, StreamersApi, WatchStreamMonitor):
    _instance = weakref.WeakValueDictionary()
    _new_lock = threading.Lock()
    _auth_lock = threading.Lock()

    def __new__(cls, user_id: int, cookies: list[dict[str, Any]]) -> "VKVideoApi":
        str_user_id = str(user_id)
        with VKVideoApi._new_lock:
            if str_user_id not in VKVideoApi._instance:
                instance = super().__new__(cls)
                VKVideoApi._instance[str_user_id] = instance
            return VKVideoApi._instance[str_user_id]

    def __init__(self, user_id: int, cookies: list[dict[str, Any]]):
        super().__init__(user_id, cookies)
        if user_id <= 0:
            return
        if hasattr(self, '_initialized'):
            self.cookies = cookies
            return

        self._initialized = True
        self.__is_running = False

        web_socket_api = WebSocketManager.get_or_create_web_socket_manager(self)
        if web_socket_api is None:
            raise RuntimeError(f"Failed to initialize WebSocketManager for user_id={self.user_id}")
        self.web_socket_api: WebSocketManager = web_socket_api
        self.heartbeat_streamers: dict[str, HeartbeatApi] = {}

        self.is_watch_online_subscribers = False
        self.is_watch_all_subscribers = False
        self.sub_streamers: list[tuple[str, int]] = []

        self.is_watch_drop_streamers = False
        self.drop_streamers: list[tuple[str, int]] = []

        self.is_watch_catalog_streamers = False
        self.catalog_id: str = ""
        self.catalog_streamers: list[tuple[str, int]] = []

        self.metrics_manager: MetricsManager | None = None

    @classmethod
    def start_auth(cls) -> "VKVideoApi":
        with cls._auth_lock:
            new_cookies = AuthModule().auth_from_selenium()
            return cls.__get_vkvideo_api_from_cookie(new_cookies)

    def refresh_auth(self) -> "VKVideoApi":
        with VKVideoApi._auth_lock:
            new_cookies = AuthModule().refresh_from_selenium(self.cookies)
            return self.__get_vkvideo_api_from_cookie(new_cookies)

    @staticmethod
    def __get_vkvideo_api_from_cookie(cookies: list[dict[str, Any]]) -> "VKVideoApi":
        instance = object.__new__(VKVideoApi)
        instance.__init__(user_id=-1, cookies=cookies)
        user_info = instance.current_user_info()
        return VKVideoApi(user_id=user_info['id'], cookies=cookies)

    def inc_metric(self, metric_name: str, amount: float = 1.0, **labels: Any) -> bool:
        if not hasattr(self, 'metrics_manager') or not self.metrics_manager:
            return False

        return self.metrics_manager.inc_metric(metric_name, amount, **labels)

    def set_gauge(self, metric_name: str, value: float, **labels: Any) -> bool:
        if not hasattr(self, 'metrics_manager') or not self.metrics_manager:
            return False

        return self.metrics_manager.set_gauge(metric_name, value, **labels)
