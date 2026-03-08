import json
import pathlib
import re
import threading
from typing import TYPE_CHECKING, Optional, Tuple

import websocket
from loguru import logger
from websocket import WebSocket

from .wss_class import WSSEventClass, WSSEventName
from ..config import WSS_URL, WSS_TYPE_MESSAGE_RE, BASE_URL

if TYPE_CHECKING:
    from ..vkvideo_main import VKVideoApi


class WebSocketClientApi:
    is_debug = False
    _run_lock = threading.Lock()

    def __init__(self, vk_api: "VKVideoApi"):
        self.vk_api = vk_api
        self.__wss: Optional[WebSocket] = None
        self.__wss_token: Optional[str] = None
        self.__wss_req_id = 1
        self.__wss_timeout = 30
        self.__is_run = False

        self._read_thread: Optional[threading.Thread] = None
        self.__streamer_subscribe = {}
        self.__callback = self.vk_api.callback
        self.streamers: dict[str, int]= {}

    def connect(self) -> None:
        with self._run_lock:
            if self.__is_run:
                return
            if not self.__wss_token:
                user_data = self.vk_api.current_user_info()
                self.__wss_token = user_data['webSocket']['token']

            self.__wss = websocket.create_connection(
                WSS_URL,
                enable_multithread=True,
                timeout=self.__wss_timeout,
                origin=BASE_URL.rstrip("/")
            )
            self._read_thread = threading.Thread(target=self._read_loop, daemon=True)
            self._read_thread.start()
            self.__send_token()
            self.__is_run = True

    def close(self):
        """Корректное закрытие соединения."""
        if self._read_thread and self._read_thread.is_alive():
            self._read_thread.join(timeout=2.0)

        if not self.__wss:
            return
        logger.debug("Closing WebSocket...")
        self.__wss.close()
        self.__wss = None
        self.__is_run = False

    def subscribe_streamer(self, streamer_nickname: str = None, streamer_id: int = None):
        if not streamer_id and not streamer_nickname:
            return

        if not self.__is_run:
            self.connect()

        if not streamer_id:
            streamer_info = self.vk_api.get_streamer_info(streamer_nickname)
            streamer_id = streamer_info.owner.id
        self.streamers[streamer_nickname.lower()] = streamer_id

        if str(streamer_id) in self.__streamer_subscribe:
            return

        stream_info = self.vk_api.get_streamer_stream_info(streamer_nickname)
        if not stream_info.data.stream:
            return
        all_ws_channels = {
            value
            for key, value in stream_info.data.stream._data_json.items()
            if isinstance(value, str) and key.startswith("ws") and str(streamer_id) in value
        }

        for channel in all_ws_channels:
            self.send({"subscribe": {"channel": channel}, "id": self.__get_wss_req_id()})
        self.__streamer_subscribe[str(streamer_id)] = all_ws_channels

    def unsubscribe_streamer(self, streamer_nickname: str = None, streamer_id: int = None):
        if not streamer_id and not streamer_nickname:
            return

        if not self.__is_run:
            return

        if not streamer_id:
            streamer_info = self.vk_api.get_streamer_info(streamer_nickname)
            streamer_id = streamer_info.owner.id

        if str(streamer_id) not in self.__streamer_subscribe:
            return

        for channel in self.__streamer_subscribe[str(streamer_id)]:
            self.send({"unsubscribe": {"channel": channel}, "id": self.__get_wss_req_id()})
        del self.__streamer_subscribe[str(streamer_id)]

    def send(self, data: dict):
        if isinstance(data, (dict, list)):
            data = json.dumps(data)
        self.__wss.send(data)
        # logger.debug(f"Message send: {data}")

    def __send_token(self):
        self.send(
            {
                "connect": {
                    "name": "js",
                    "token": self.__wss_token,
                },
                "id": self.__get_wss_req_id()
            }
        )

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

    def _read_loop(self):
        """Основной цикл чтения сообщений."""
        self.__wss.timeout = self.__wss_timeout

        try:
            while self.__wss.connected:
                try:
                    message = self.__wss.recv()
                    if message is None:
                        logger.debug("Server closed connection.")
                        break

                    try:
                        for obj in self.__decode_json_stream(message):
                            if obj == {}:
                                self.send({})
                                continue

                            self.__send_callback(obj)
                            # logger.debug(f"Message received: {obj}")
                    except:  # noqa
                        logger.exception(f"Пришло нестандартное сообщение {message=}")

                except websocket.WebSocketTimeoutException:
                    continue
                except websocket.WebSocketConnectionClosedException:
                    logger.warning("Connection closed unexpectedly.")
                    break
                except Exception as e:
                    logger.error(f"Error receiving message: {e}")
                    break

        finally:
            self.close()

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
                return

        self.debug_save_message(message)

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

    def debug_save_message(self, message: dict) -> None:
        if not self.is_debug:
            return

        path_save = pathlib.Path("data") / "wss_message"
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
