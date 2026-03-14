import json
import random
import re
import threading
import time
from typing import TYPE_CHECKING, Optional, Tuple

import websocket
from loguru import logger
from websocket import WebSocket

from app_vkvideo.config import Config as MainConfig
from .wss_class import *
from ..api.api_class import *
from ..config import WSS_URL, WSS_TYPE_MESSAGE_RE, BASE_URL

if TYPE_CHECKING:
    from ..vkvideo_main import VKVideoApi


class WebSocketManager:
    _lock_create_wss_manager = threading.Lock()
    _lock_debug_message_save = threading.Lock()
    _wss_manager_dict: dict[str, "WebSocketManager"] = {}

    def __init__(self, vk_api: "VKVideoApi"):
        self.user_id: int = vk_api.user_id
        self.vk_api = vk_api

        self.web_socket: Optional[WebSocket] = None

        self.streamer_nickname_active: set[str] = set()
        self.streamer_nickname_subscribe: set[str] = set()
        self.streamer_web_socket_channels: dict[str, set] = {}

        self._web_socket_request_id = 0
        self._web_socket_timeout = 30
        self._web_socket_is_auth = False

        self._lock_connect = threading.Lock()
        self._lock_subscribe = threading.Lock()
        self._thread_read_message: Optional[threading.Thread] = None
        self._thread_stop_event = threading.Event()
        self._reconnect_attempt = 0
        self._reconnect_scheduled = False

    @classmethod
    def get_or_create_wss_manager(cls, vk_api: "VKVideoApi") -> Optional["WebSocketManager"]:
        if not vk_api or not getattr(vk_api, "user_id", None):
            return None
        str_user_id = str(vk_api.user_id)
        with cls._lock_create_wss_manager:
            if str_user_id in cls._wss_manager_dict:
                return cls._wss_manager_dict[str_user_id]
            cls._wss_manager_dict[str_user_id] = WebSocketManager(vk_api)
            return cls._wss_manager_dict[str_user_id]

    @staticmethod
    def normalize_send_message(message: str | dict | list) -> str:
        if isinstance(message, dict):
            return json.dumps(message)
        elif isinstance(message, list):
            return "\n".join([json.dumps(m) if isinstance(m, dict) else str(m) for m in message])
        else:
            return str(message)

    def is_connected(self) -> bool:
        if not self.web_socket or not self.web_socket.connected:
            return False
        elif not self._thread_read_message or not self._thread_read_message.is_alive():
            return False
        elif self._thread_stop_event.is_set():
            return False
        return True

    def connect(self):
        try:
            with self._lock_connect:
                if self.is_connected():
                    return

                self._thread_stop_event.set()
                self._web_socket_request_id = 0

                web_socket_token = self._fetch_user_web_socket_token()
                logger.info(f"[{self.vk_api.user_id}] WebSocket: Подключаюсь к VKLive")
                self.web_socket = websocket.create_connection(
                    WSS_URL, enable_multithread=True, origin=BASE_URL.rstrip("/"), timeout=self._web_socket_timeout
                )
                logger.info(
                    f"[{self.user_id}] WebSocket: Статус соединения к VKLive: status={self.web_socket.connected}"
                )

                if self._thread_read_message and self._thread_read_message.is_alive():
                    if self._thread_read_message != threading.current_thread():
                        self._thread_read_message.join(timeout=10)

                self._thread_stop_event.clear()
                self._thread_read_message = threading.Thread(target=self._loop_read_message, daemon=True)
                self._thread_read_message.start()

                self._auth_user_web_socket_token(web_socket_token)
                self.vk_api.set_gauge("vkapp_wss_active", 1)
                self._reconnect_attempt = 0
        except Exception:  # noqa
            logger.exception(f"[{self.user_id}] WebSocket: Ошибка подключения.", exc_info=True)
        finally:
            if not self.is_connected():
                self.disconnect(is_reconnect=True)

    def disconnect(self, is_reconnect: bool = False):
        try:
            with self._lock_connect:
                self._web_socket_is_auth = False
                self._thread_stop_event.set()

                if self.web_socket:
                    if self.web_socket.connected:
                        logger.info(f"[{self.user_id}]: Закрываю WebSocket соединение...")
                        self.web_socket.close(timeout=self._web_socket_timeout)
                    self.web_socket = None

                if self._thread_read_message and self._thread_read_message.is_alive():
                    if self._thread_read_message != threading.current_thread():
                        self._thread_read_message.join(timeout=10)

                self.streamer_nickname_active = set()
                if not is_reconnect:
                    self.streamer_nickname_subscribe = set()

                self.vk_api.callback.trigger(WSSEventName.ON_DISCONNECTED, user_id=self.user_id)
                self.vk_api.set_gauge("vkapp_wss_active", 0)
        except Exception:  # noqa
            logger.exception(f"[{self.user_id}] WebSocket: Ошибка отключения.", exc_info=True)
        finally:
            if is_reconnect:
                threading.Thread(target=self._schedule_reconnect, daemon=True).start()

    def _schedule_reconnect(self):
        if self._reconnect_scheduled:
            return
        self._reconnect_scheduled = True
        self._reconnect_attempt += 1
        delay = min(30.0, (2 ** min(self._reconnect_attempt, 5)) + random.random())
        logger.info(f"[{self.user_id}] WebSocket: Переподключение через {delay:.1f}s (attempt={self._reconnect_attempt})")
        time.sleep(delay)
        self._reconnect_scheduled = False

        wss_api = getattr(self.vk_api, "wss_api", None)
        if wss_api is not None and not wss_api.is_run:
            return
        self.connect()

    def subscribe_streamer(self, streamer_nickname: str, web_socket_channels: list | set | None):
        if not streamer_nickname:
            return

        clear_streamer_nickname = str(streamer_nickname).lower()
        if web_socket_channels and clear_streamer_nickname not in self.streamer_web_socket_channels:
            if isinstance(web_socket_channels, list):
                web_socket_channels = set(web_socket_channels)
            self.streamer_web_socket_channels[clear_streamer_nickname] = web_socket_channels

        self.streamer_nickname_subscribe.add(clear_streamer_nickname)
        self._send_subscribe_message(clear_streamer_nickname)

    def _send_subscribe_message(self, streamer_nickname: str):
        with self._lock_subscribe:
            if not self._web_socket_is_auth:
                return

            clear_streamer_nickname = str(streamer_nickname).lower()
            web_socket_channels = self.streamer_web_socket_channels.get(clear_streamer_nickname, set())
            if not web_socket_channels:
                return
            if clear_streamer_nickname in self.streamer_nickname_active:
                return

            messages = [
                {
                    "subscribe": {
                        "channel": c
                    },
                    "id": self._generate_request_id()
                }
                for c in web_socket_channels
            ]
            if not self._send_message(messages):
                return

            self.streamer_nickname_active.add(clear_streamer_nickname)
            self.vk_api.inc_metric("vkapp_wss_subscriptions_total")
            logger.info(
                f"[{self.user_id}] WebSocket: "
                f"Подписался на {len(messages)} событий стримера '[{clear_streamer_nickname}]'"
            )

    def unsubscribe_streamer(self, streamer_nickname: str):
        if not streamer_nickname:
            return

        clear_streamer_nickname = str(streamer_nickname).lower()
        if clear_streamer_nickname not in self.streamer_nickname_subscribe:
            return
        if clear_streamer_nickname not in self.streamer_web_socket_channels:
            return

        self.streamer_nickname_subscribe.remove(clear_streamer_nickname)
        self._send_unsubscribe_message(clear_streamer_nickname)

    def _send_unsubscribe_message(self, streamer_nickname: str):
        with self._lock_subscribe:
            if not self._web_socket_is_auth:
                return

            clear_streamer_nickname = str(streamer_nickname).lower()
            web_socket_channels = self.streamer_web_socket_channels.get(clear_streamer_nickname, set())
            if not web_socket_channels:
                return
            if clear_streamer_nickname not in self.streamer_nickname_active:
                return

            messages = [
                {
                    "unsubscribe": {
                        "channel": c
                    },
                    "id": self._generate_request_id()
                }
                for c in web_socket_channels
            ]
            if not self._send_message(messages):
                return

            self.streamer_nickname_active.remove(clear_streamer_nickname)
            self.vk_api.inc_metric("vkapp_wss_unsubscriptions_total")
            logger.info(
                f"[{self.user_id}] WebSocket: "
                f"Отписался от {len(messages)} событий стримера '[{clear_streamer_nickname}]'"
            )

    def update_web_socket_channels(self, streamer_nickname: str, web_socket_channels: list | set | None):
        if not streamer_nickname or not web_socket_channels:
            return

        clear_streamer_nickname = str(streamer_nickname).lower()

        is_active = clear_streamer_nickname in self.streamer_nickname_active
        is_subscribe = clear_streamer_nickname in self.streamer_nickname_subscribe

        if isinstance(web_socket_channels, list):
            web_socket_channels = set(web_socket_channels)
        old_channels = self.streamer_web_socket_channels.get(clear_streamer_nickname)
        self.streamer_web_socket_channels[clear_streamer_nickname] = web_socket_channels

        if old_channels is not None and old_channels != web_socket_channels and (is_active or is_subscribe):
            self.streamer_web_socket_channels[clear_streamer_nickname] = old_channels
            self._send_unsubscribe_message(clear_streamer_nickname)
            self.streamer_web_socket_channels[clear_streamer_nickname] = web_socket_channels
            self._send_subscribe_message(clear_streamer_nickname)
            return

        if is_active or not is_subscribe:
            return
        self._send_subscribe_message(streamer_nickname)

    def _check_all_subscribe_streamer(self):
        self.vk_api.set_gauge("vkapp_wss_streamers_all", float(len(self.streamer_nickname_subscribe)))
        self.vk_api.set_gauge("vkapp_wss_streamers_active", float(len(self.streamer_nickname_active)))

        add_list = self.streamer_nickname_subscribe - self.streamer_nickname_active
        for streamer_nickname in add_list:
            self._send_subscribe_message(streamer_nickname)

        del_list = self.streamer_nickname_active - self.streamer_nickname_subscribe
        for streamer_nickname in del_list:
            self._send_unsubscribe_message(streamer_nickname)

    def _fetch_user_web_socket_token(self):
        logger.info(f"[{self.user_id}] WebSocket: Получаю токен пользователя для WebSocket соединения...")
        user_data = self.vk_api.current_user_info()
        token = user_data.get('webSocket', {}).get('token')
        if not token:
            raise RuntimeError("Не удалось получить WebSocket token")
        logger.info(f"[{self.user_id}] WebSocket: Токен WSS соединения получен '{token[:10]}...'")
        return token

    def _auth_user_web_socket_token(self, web_socket_token: str):
        message = {
            "connect": {
                "name": "js",
                "token": web_socket_token,
            },
            "id": self._generate_request_id()
        }
        ws = self.web_socket
        if not ws or not ws.connected:
            raise RuntimeError("WebSocket не готов к авторизации")
        ws.send(self.normalize_send_message(message))
        logger.info(f"[{self.user_id}] WebSocket: Отправил запрос на авторизацию в VKLive")

    def _generate_request_id(self) -> int:
        self._web_socket_request_id += 1
        return self._web_socket_request_id

    def _send_message(self, message: dict | list | str) -> bool:
        self.vk_api.inc_metric("vkapp_wss_requests")
        message = self.normalize_send_message(message)
        if not message:
            return False
        if not self.is_connected():
            return False
        ws = self.web_socket
        if not ws or not ws.connected:
            return False
        ws.send(message)
        # logger.debug(f"[{self.user_id}] WebSocket: Отправил запрос: '{message=}'.")
        return True

    def _loop_read_message(self):
        ws = self.web_socket
        if not ws:
            return
        try:
            while ws.connected:
                try:
                    if not self.is_connected():
                        break

                    message_str = ws.recv()
                    if message_str is None:
                        logger.error(f"[{self.user_id}] WebSocket: VKLive закрыл соединение.")
                        break

                    try:
                        for message_dict in self._decode_json_stream(message_str):
                            threading.Thread(target=self._check_message, args=(message_dict,), daemon=True).start()
                    except:  # noqa
                        logger.error(
                            f"[{self.user_id}] WebSocket: Пришло нестандартное сообщение '{message_str=}'",
                            exc_info=True
                        )
                except websocket.WebSocketTimeoutException:
                    continue
                except websocket.WebSocketConnectionClosedException:
                    logger.error(f"[{self.user_id}] WebSocket: Соединение неожиданно прервалось.", exc_info=True)
                    break
                except Exception:  # noqa
                    logger.error(f"[{self.user_id}] WebSocket: Непредвиденная ошибка соединения.", exc_info=True)
                    break
        finally:
            if not self._thread_stop_event.is_set():
                threading.Thread(target=self.disconnect, kwargs={"is_reconnect": True}).start()

    @staticmethod
    def _decode_json_stream(stream):
        decoder = json.JSONDecoder()
        _idx = 0
        while _idx < len(stream):
            _obj, _end = decoder.raw_decode(stream, _idx)
            yield _obj
            _idx = _end
            while _idx < len(stream) and stream[_idx] in '\n ':
                _idx += 1

    def _check_message(self, message: dict):
        self.vk_api.inc_metric("vkapp_wss_responses")

        message_str = str(message)
        if "connect" in message_str and "client" in message_str and "version" in message_str and "expires" in message_str:
            self._web_socket_is_auth = True
            self.vk_api.callback.trigger(WSSEventName.ON_CONNECTED, user_id=self.user_id)
            logger.info(f"[{self.user_id}] WebSocket: Успешная авторизация пользователя. {message_str=}")
            self.vk_api.inc_metric("vkapp_wss_message_type_response_total", message_name="success_auth")

        if message == {}:
            self._send_message("{}")
            threading.Thread(target=self._check_all_subscribe_streamer, daemon=True).start()
            self.vk_api.inc_metric("vkapp_wss_message_type_response_total", message_name="ping")
            return

        self._trigger_message_callback(message)
        self._debug_save_message(message)

    @staticmethod
    def _get_message_type_info(message: dict) -> Tuple[Optional[str], Optional[int], Optional[int]]:
        try:
            message_type = message['push']['pub']['data']['type']
            channel = message['push']['channel']
        except (KeyError, TypeError):
            return None, None, None
        if not channel or not message_type:
            return None, None, None

        match = re.search(WSS_TYPE_MESSAGE_RE, channel)
        if not match:
            return None, None, None

        channel_type = match.group(1)
        streamer_id = match.group(2)
        streamer_id_int = int(streamer_id) if streamer_id and streamer_id.isdigit() else None
        user_id = match.group(3)
        user_id_int = int(user_id) if user_id and user_id.isdigit() else None

        _normalize_text = re.sub(r"[^a-zA-Z]+", "_", str(f"{message_type}_{channel_type}"))
        clear_channel_type = re.sub(r"_+", "_", _normalize_text).strip("_").lower()
        return clear_channel_type, streamer_id_int, user_id_int

    def _trigger_message_callback(self, message: dict):
        channel_type, streamer_id, user_id = self._get_message_type_info(message)
        if not channel_type or not streamer_id:
            return
        self.vk_api.inc_metric("vkapp_wss_message_type_response_total", message_name=channel_type)

        self.vk_api.callback.trigger(WSSEventName.ON_MESSAGE, streamer_id=streamer_id, user_id=user_id, message=message)
        for event, _class in WSSEventClass.items():
            if event.value == channel_type:
                self.vk_api.callback.trigger(event, streamer_id=streamer_id, user_id=user_id, message=_class(message))
                break

    def _debug_save_message(self, message: dict) -> None:
        if True:
            return
        # if not self.is_debug:
        #     return

        with self._lock_debug_message_save:
            path_save = MainConfig.DATA_PATH / "wss_message"
            path_save.mkdir(parents=True, exist_ok=True)

            file_name, _, _ = self._get_message_type_info(message)
            if not file_name:
                return

            file_path = path_save / f"{file_name}.json"
            saved_data = []
            if file_path.is_file():
                try:
                    saved_data = json.loads(file_path.read_text(encoding="utf-8"))
                    if not isinstance(saved_data, list):
                        saved_data = []
                except (json.JSONDecodeError, OSError):
                    saved_data = []

            saved_data.append(message)
            if len(saved_data) > 100:
                saved_data = saved_data[-100:]

            temp_path = file_path.with_suffix('.tmp')
            str_save_data = json.dumps(saved_data, ensure_ascii=False, indent=2, sort_keys=True)
            try:
                temp_path.write_text(str_save_data, encoding="utf-8")
                temp_path.replace(file_path)
            except OSError:
                file_path.write_text(str_save_data, encoding="utf-8")
                if temp_path.exists():
                    temp_path.unlink()


class WebSocketClientApi:
    is_debug = False

    def __init__(self, vk_api: "VKVideoApi"):
        self.vk_api = vk_api
        self.callback = self.vk_api.callback

        self.wss_manager: Optional[WebSocketManager] = WebSocketManager.get_or_create_wss_manager(self.vk_api)
        self.__is_run: bool = False

        self._initialize_callback()

    @property
    def is_run(self) -> bool:
        return self.__is_run

    @is_run.setter
    def is_run(self, is_run: bool) -> None:
        if not isinstance(is_run, bool) or self.__is_run == is_run:
            return
        self.__is_run = is_run

        if not self.wss_manager: return
        if self.__is_run:
            self.wss_manager.connect()
        else:
            self.wss_manager.disconnect()

    def subscribe_streamer(self, streamer_nickname: str, web_socket_channels: list | set | None = None):
        if not streamer_nickname: return
        self.is_run = True
        if not self.wss_manager: return
        self.wss_manager.subscribe_streamer(streamer_nickname, web_socket_channels)

    def unsubscribe_streamer(self, streamer_nickname: str):
        if not streamer_nickname: return
        if not self.wss_manager: return
        self.wss_manager.unsubscribe_streamer(streamer_nickname)

    @staticmethod
    def generate_web_socket_channel_from_dict(data: dict, streamer_id: int | str) -> set:
        if not streamer_id or not data or not isinstance(data, dict):
            return set()

        str_streamer_id = str(streamer_id)
        return {
            value
            for key, value in data.items()
            if key.startswith("ws") and isinstance(value, str) and str_streamer_id in value
        }

    def _initialize_callback(self) -> None:
        if hasattr(self, "__init_callback"):
            return
        self.__init_callback = True
        self.vk_api.callback.register(VKAPIEventName.STREAMER_STREAM_INFO, self.__on_streamer_stream_info)
        self.vk_api.callback.register(VKAPIEventName.ONLINE_SUBSCRIPTION_STREAMERS, self.__on_online_subscription_streamers)
        self.vk_api.callback.register(VKAPIEventName.DROP_STREAMERS, self.__on_drop_streamers)
        self.vk_api.callback.register(VKAPIEventName.CATALOG_STREAMERS, self.__on_catalog_streamers)
        # self.vk_api.callback.register(WSSEventName.ON_DISCONNECTED, self.__on_disconnected)

    def __on_streamer_stream_info(self, streamer_id: int, user_id: int, message: VkapiStreamerStreamInfo):
        if not self.wss_manager: return
        if str(user_id) != str(self.vk_api.user_id): return
        streamer_nickname = message.data.stream.embed_url.split("/")[-1]
        _streamer_id = message.data.stream.user.id
        _data_dict = message.data.stream._data_json
        all_ws_channels = self.generate_web_socket_channel_from_dict(_data_dict, streamer_id=_streamer_id)
        if not all_ws_channels: return
        self.wss_manager.update_web_socket_channels(streamer_nickname, all_ws_channels)

    def __on_online_subscription_streamers(self, user_id: int, message: VkapiOnlineSubscriptionStreamers):
        if not self.wss_manager: return
        if str(user_id) != str(self.vk_api.user_id): return
        for stream_blog in message.data.stream_blogs:
            stream_json = stream_blog.stream._data_json
            streamer_id = stream_blog.blog.owner.id
            streamer_nickname = stream_blog.blog.blog_url
            all_ws_channels = self.generate_web_socket_channel_from_dict(stream_json, streamer_id=streamer_id)

            if not all_ws_channels: continue
            self.wss_manager.update_web_socket_channels(streamer_nickname, all_ws_channels)

    def __on_drop_streamers(self, user_id: int, message: VkapiDropStreamers):
        if not self.wss_manager: return
        if str(user_id) != str(self.vk_api.user_id): return
        for stream_blog in message.data.stream_blogs:
            stream_json = stream_blog.stream._data_json
            streamer_id = stream_blog.blog.owner.id
            streamer_nickname = stream_blog.blog.blog_url
            all_ws_channels = self.generate_web_socket_channel_from_dict(stream_json, streamer_id=streamer_id)

            if not all_ws_channels: continue
            self.wss_manager.update_web_socket_channels(streamer_nickname, all_ws_channels)

    def __on_catalog_streamers(self, user_id: int, message: VkapiCatalogStreamers):
        if not self.wss_manager: return
        if str(user_id) != str(self.vk_api.user_id): return
        for stream_blog in message.data.stream_blogs:
            stream_json = stream_blog.stream._data_json
            streamer_id = stream_blog.blog.owner.id
            streamer_nickname = stream_blog.blog.blog_url
            all_ws_channels = self.generate_web_socket_channel_from_dict(stream_json, streamer_id=streamer_id)

            if not all_ws_channels: continue
            self.wss_manager.update_web_socket_channels(streamer_nickname, all_ws_channels)
