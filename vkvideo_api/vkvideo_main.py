import threading
import weakref
from typing import Any

from .api import UserApi, StreamerApi, StreamersApi, WatchStreamMonitor
from .auth import AuthModule
from .heartbeat import WebSocketClientApi, HeartbeatApi


class VKVideoApi(UserApi, StreamerApi, StreamersApi, WatchStreamMonitor):
    _instance = weakref.WeakValueDictionary()
    _new_lock = threading.Lock()
    _auth_lock = threading.Lock()

    def __new__(cls, account_id: int, cookies: list[dict[str, Any]]) -> "VKVideoApi":
        str_account_id = str(account_id)
        with VKVideoApi._new_lock:
            if str_account_id not in VKVideoApi._instance:
                instance = super().__new__(cls)
                VKVideoApi._instance[str_account_id] = instance
            return VKVideoApi._instance[str_account_id]

    def __init__(self, account_id: int, cookies: list[dict[str, Any]]):
        super().__init__(account_id, cookies)
        if hasattr(self, '_initialized'):
            self.cookies = cookies
            return

        self._initialized = True
        self.__is_running = False

        self.wss_api = WebSocketClientApi(self)
        self.streamers: dict[str, HeartbeatApi] = {}

        self.is_watch_all_subscribers = False
        self.sub_streamers: list[tuple[str, int]] = []

        self.is_watch_drop_streamers = False
        self.drop_streamers: list[tuple[str, int]] = []

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
        instance.__init__(account_id=-1, cookies=cookies)
        user_info = instance.current_user_info()
        return VKVideoApi(account_id=user_info['id'], cookies=cookies)
