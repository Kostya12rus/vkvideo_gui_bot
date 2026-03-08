import json
import random
import re
import threading
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


class WebSocketClientApi:
    is_debug = False

    def __init__(self, vk_api: "VKVideoApi"):
        self.vk_api = vk_api
        self.streamer_subscribe: dict[str, set] = {}

        self.__callback = self.vk_api.callback

        self.__wss: Optional[WebSocket] = None
        self.__wss_token: Optional[str] = None
        self.__wss_req_id = 0
        self.__wss_timeout = 30

        self.__is_run: bool = False
        self.__lock_connect = threading.Lock()
        self.__lock_debug_message = threading.Lock()
        self.__thread_read_message: Optional[threading.Thread] = None
        self.__thread_stop_event = threading.Event()

    @property
    def is_run(self) -> bool:
        return self.__is_run

    @is_run.setter
    def is_run(self, is_run: bool) -> None:
        if not isinstance(is_run, bool) or self.__is_run == is_run:
            return
        self.__is_run = is_run

        self._initialize_callback()
        if self.__is_run:
            self._connect()
        else:
            self._close()

    def _connect(self) -> None:
        with self.__lock_connect:
            if self.__wss and self.__wss.connected:
                return

            if not self.__wss_token:
                logger.info(f"[{self.vk_api.user_id}]: Получаю токен пользователя для WSS соединения...")
                user_data = self.vk_api.current_user_info()
                self.__wss_token = user_data['webSocket']['token']
                logger.info(f"[{self.vk_api.user_id}]: Токен WSS соединения получен '{self.__wss_token[:10]}...'")

            logger.info(f"[{self.vk_api.user_id}]: Подключаю WSS соединения к VKLive")
            self.__wss = websocket.create_connection(
                WSS_URL,
                enable_multithread=True,
                timeout=self.__wss_timeout,
                origin=BASE_URL.rstrip("/")
            )
            logger.info(f"[{self.vk_api.user_id}]: Статус WSS соединения к VKLive: status={self.__wss.connected}")

            self.__thread_stop_event.clear()
            self.__thread_read_message = threading.Thread(target=self._loop_read_message, daemon=True)
            self.__thread_read_message.start()

            self.__send_token()
            logger.info(f"[{self.vk_api.user_id}]: Авторизовался в WSS соединения к VKLive")

    def _close(self):
        with self.__lock_connect:
            if self.__wss:
                if self.__wss.connected:
                    logger.debug("Closing WebSocket...")
                    self.__wss.close()
                self.__wss = None

            self.__thread_stop_event.set()
            if self.__thread_read_message and self.__thread_read_message.is_alive():
                self.__thread_read_message.join(timeout=2.0)

            self.__is_run = False
            self.__wss_req_id = 0
            self.streamer_subscribe = {}

    def subscribe_streamer(self, streamer_nickname: str = None):
        if not streamer_nickname:
            return
        self.is_run = True

        clear_streamer_nickname = str(streamer_nickname).lower()
        if clear_streamer_nickname not in self.streamer_subscribe:
            self.streamer_subscribe[clear_streamer_nickname] = set()

        streamer_wss_channels = self.streamer_subscribe.get(clear_streamer_nickname, set())
        if not streamer_wss_channels:
            heartbeat_class = self.vk_api.get_heartbeat_class(streamer_nickname=streamer_nickname)
            if heartbeat_class and heartbeat_class._last_streamer_stream_info:
                streamer_wss_channels = self.__generate_wss_channel_from_data(heartbeat_class._last_streamer_stream_info)
                if streamer_wss_channels:
                    self.streamer_subscribe[streamer_nickname] = streamer_wss_channels
        if not streamer_wss_channels:
            return

        messages = [{"subscribe": {"channel": c}, "id": self.__get_wss_req_id()} for c in streamer_wss_channels]
        self._send_message("\n".join([json.dumps(m) for m in messages]))

        logger.info(
            f"[{self.vk_api.user_id}]: [{clear_streamer_nickname}] "
            f"Подписался на {len(streamer_wss_channels)} событий стримера"
        )

    def unsubscribe_streamer(self, streamer_nickname: str = None):
        if not not self.__is_run or not streamer_nickname:
            return

        clear_streamer_nickname = str(streamer_nickname).lower()
        if clear_streamer_nickname not in self.streamer_subscribe:
            return

        streamer_wss_channels = self.streamer_subscribe.get(clear_streamer_nickname, set())
        if not streamer_wss_channels:
            heartbeat_class = self.vk_api.get_heartbeat_class(streamer_nickname=streamer_nickname)
            if heartbeat_class and heartbeat_class._last_streamer_stream_info:
                streamer_wss_channels = self.__generate_wss_channel_from_data(heartbeat_class._last_streamer_stream_info)
                if streamer_wss_channels:
                    self.streamer_subscribe[streamer_nickname] = streamer_wss_channels

        messages = [{"unsubscribe": {"channel": c}, "id": self.__get_wss_req_id()} for c in streamer_wss_channels]
        self._send_message("\n".join([json.dumps(m) for m in messages]))

        logger.info(
            f"[{self.vk_api.user_id}]: [{clear_streamer_nickname}] "
            f"Отписался от {len(streamer_wss_channels)} событий стримера"
        )
        del self.streamer_subscribe[clear_streamer_nickname]

    def _send_message(self, message: dict | list | str):
        if isinstance(message, (dict, list)):
            message = json.dumps(message)
        elif isinstance(message, str):
            pass
        else:
            return
        if message == "{}":
            self.__wss.send(message)
            # logger.debug(f"Message send: {message}")
            return
        elif "connect" in message and "token" in message:
            self.__wss.send(message)
            # logger.debug(f"Message send: TOKEN SECRIT")
            return

        with self.__lock_connect:
            if not self.__wss.connected:
                return
            self.__wss.send(message)
            # logger.debug(f"Message send: {message}")

    def _loop_read_message(self):
        """Основной цикл чтения сообщений."""
        self.__wss.timeout = self.__wss_timeout

        try:
            while self.__wss.connected:
                try:
                    if self.__thread_stop_event.is_set():
                        break

                    message = self.__wss.recv()
                    if message is None:
                        logger.debug("Server closed connection.")
                        break

                    try:
                        for obj in self.__decode_json_stream(message):
                            threading.Thread(target=self.__thread_check_message, args=(obj,), daemon=True).start()
                    except:  # noqa
                        logger.error(f"Пришло нестандартное сообщение {message=}")

                except websocket.WebSocketTimeoutException:
                    continue
                except websocket.WebSocketConnectionClosedException:
                    logger.error("WSS Connection closed unexpectedly.", exc_info=True)
                    break
                except Exception:  # noqa
                    logger.error(f"WSS Connection closed error receiving message.", exc_info=True)
                    break
        finally:
            if self.__is_run and not self.__wss.connected:
                self.__wss_token = ""
                if self.__thread_stop_event.wait(random.randint(1, 5) + random.random()):
                    return 
                self._connect()

    def __thread_check_message(self, message: dict):
        # logger.debug(f"Message received: {message}")
        if message == {}:
            self._send_message({})
            return

        self.__send_callback(message)

    def __send_token(self):
        self._send_message({
            "connect": {
                "name": "js",
                "token": self.__wss_token,
            },
            "id": self.__get_wss_req_id()
        })

    def __get_wss_req_id(self) -> int:
        self.__wss_req_id += 1
        return self.__wss_req_id

    @staticmethod
    def __decode_json_stream(stream):
        decoder = json.JSONDecoder()
        _idx = 0
        while _idx < len(stream):
            _obj, _end = decoder.raw_decode(stream, _idx)
            yield _obj
            _idx = _end
            while _idx < len(stream) and stream[_idx] in '\n ':
                _idx += 1

    def __send_callback(self, message: dict):
        channel_type, streamer_id, user_id = self.__get_message_type_info(message)
        if not channel_type or not streamer_id:
            return

        self.__callback.trigger(WSSEventName.ON_MESSAGE, streamer_id=streamer_id, user_id=user_id, message=message)

        for event, _class in WSSEventClass.items():
            if event.value == channel_type:
                self.__callback.trigger(
                    event, streamer_id=streamer_id, user_id=user_id, message=_class(message)
                )
                break

        self.__debug_save_message(message)

    @staticmethod
    def __get_message_type_info(message: dict) -> Tuple[Optional[str], Optional[int], Optional[int]]:
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

    def __debug_save_message(self, message: dict) -> None:
        if not self.is_debug:
            return

        with self.__lock_debug_message:
            path_save = MainConfig.DATA_PATH / "wss_message"
            path_save.mkdir(parents=True, exist_ok=True)

            file_name, _, _ = self.__get_message_type_info(message)
            if not file_name:
                return

            file_path = path_save / f"{file_name}.json"
            saved_data = []
            if file_path.is_file():
                try:
                    content = file_path.read_text(encoding="utf-8")
                    saved_data = json.loads(content)
                    if not isinstance(saved_data, list):
                        saved_data = []
                except (json.JSONDecodeError, OSError):
                    saved_data = []

            saved_data.append(message)
            if len(saved_data) > 100:
                saved_data = saved_data[-100:]

            temp_path = file_path.with_suffix('.tmp')

            try:
                temp_path.write_text(
                    json.dumps(saved_data, ensure_ascii=False, indent=2),
                    encoding="utf-8"
                )
                temp_path.replace(file_path)
            except OSError:
                file_path.write_text(
                    json.dumps(saved_data, ensure_ascii=False, indent=2),
                    encoding="utf-8"
                )
                if temp_path.exists():
                    temp_path.unlink()

    def _initialize_callback(self) -> None:
        if hasattr(self, "__init_callback"):
            return
        self.__init_callback = True
        self.vk_api.callback.register(VKAPIEventName.STREAMER_STREAM_INFO, self.__on_streamer_stream_info)

    def __on_streamer_stream_info(self, streamer_id: int, user_id: int, message: VkapiStreamerStreamInfo):
        streamer_nickname = message.data.stream.embed_url.split("/")[-1]
        clear_streamer_nickname = str(streamer_nickname).lower()
        if clear_streamer_nickname not in self.streamer_subscribe:
            return

        all_ws_channels = self.__generate_wss_channel_from_data(message)
        if all_ws_channels:
            self.streamer_subscribe[clear_streamer_nickname] = all_ws_channels
            self.subscribe_streamer(streamer_nickname)

    @staticmethod
    def __generate_wss_channel_from_data(data: VkapiStreamerStreamInfo) -> set:
        if not data:
            return set()
        str_streamer_id = str(data.data.stream.user.id)
        return {
            value
            for key, value in data.data.stream._data_json.items()
            if isinstance(value, str) and key.startswith("ws") and str_streamer_id in value
        }
