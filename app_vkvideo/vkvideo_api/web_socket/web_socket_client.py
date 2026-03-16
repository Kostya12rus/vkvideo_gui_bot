import json
import random
import threading
from typing import Optional, TYPE_CHECKING

import curl_cffi
from curl_cffi import WebSocket, CurlWsFlag, WsCloseCode, WebSocketError, CurlECode, CurlInfo
from curl_cffi.aio import CURL_SOCKET_BAD
from curl_cffi.curl import CurlError
from loguru import logger
from select import select

from app_vkvideo.utils import CallbackManager
from app_vkvideo.vkvideo_api.auth import AuthModule
from app_vkvideo.vkvideo_api.config import WSS_URL, BASE_URL
from .web_socket_model import WebSocketEventName

if TYPE_CHECKING:
    from ..vkvideo_main import VKVideoApi


class CurlWsFrame:
    age: int
    flags: int
    offset: int
    bytesleft: int
    len: int


class WebSocketClient:
    def __init__(self, vk_api: "VKVideoApi"):
        self.vk_api = vk_api
        self.web_socket = WebSocket()

        self._connect_count = 0
        self._lock_run = threading.Lock()
        self._thread_run_forever: Optional[threading.Thread] = None
        self._thread_stop_event = threading.Event()

        self.__web_socket_token = ""
        self.__is_authenticated = False
        self.__callback = CallbackManager()
        self.__web_socket_request_id = 0

    def _logger_message(self, message: str):
        return f"[{self.vk_api.user_id}] WebSocket: {message}"

    def __on_open(self):
        self.__callback.trigger(WebSocketEventName.WEB_SOCKET_ON_OPEN, self)
        logger.info(self._logger_message("Отправил запрос на авторизацию в VKLive"))
        status_auth = self.web_socket.send_json(
            {
                "connect": {
                    "token": self.__web_socket_token,
                    "name": "js"
                },
                "id": 1
            }
        )
        self.__on_authenticated(status_auth > 0)

    def __on_close(self, code: int, reason: str):
        logger.exception(self._logger_message(f"Соединение с VKLive потеряно, причина: {code=}, {reason=}"))
        self.__callback.trigger(WebSocketEventName.WEB_SOCKET_ON_CLOSE, self, code, reason)
        self.__on_authenticated(status=False)

    def __on_data(self, data: bytes, frame: CurlWsFrame):
        self.__callback.trigger(WebSocketEventName.WEB_SOCKET_ON_DATA, self, data, frame)
        if data == b"{}":
            self.web_socket.send(b"{}")
            self.vk_api.inc_metric("vkapp_wss_message_type_response_total", message_name="ping")

        try:
            message_str = str(data)
            if "connect" in message_str and "client" in message_str and "version" in message_str and "expires" in message_str:
                logger.warning(self._logger_message(f"Успешная авторизация пользователя. {message_str=}"))
                self.vk_api.inc_metric("vkapp_wss_message_type_response_total", message_name="success_auth")
        except Exception as e:  # noqa
            pass

    def __on_message(self, message: str | bytes):
        if isinstance(message, bytes):
            try:
                message = message.decode("utf-8")
            except UnicodeDecodeError:
                logger.warning(self._logger_message("on_message: received non-UTF8 bytes payload"))
                return

        message_list = message.split("\n")
        for _m in message_list:
            if not _m.strip():
                continue
            try:
                message_json = json.loads(_m.strip())
                self.__callback.trigger(WebSocketEventName.WEB_SOCKET_ON_MESSAGE, self, message_json)
            except json.decoder.JSONDecodeError:
                logger.warning(self._logger_message(f"on_message: error decoding message chunk: {_m}"))
                continue

    def __on_error(self, exception: CurlError):
        logger.exception(self._logger_message(f"Ошибка в работе {exception}"))
        self.__callback.trigger(WebSocketEventName.WEB_SOCKET_ON_ERROR, self, exception)

    def __on_authenticated(self, status: bool):
        logger.info(self._logger_message(f"Статус авторизации с VKLive, статус: {status}"))
        self.__callback.trigger(WebSocketEventName.WEB_SOCKET_ON_AUTHENTICATED, self, status)
        self.__is_authenticated = status

    def __send_any(self, message: str | bytes | list | dict) -> bool:
        status = False
        try:
            if isinstance(message, dict):
                status = self.web_socket.send_json(message) > 0
            elif isinstance(message, list):
                list_str = "\n".join([json.dumps(m) if isinstance(m, dict) else str(m) for m in message])
                status = self.web_socket.send(list_str) > 0
            else:
                status = self.web_socket.send(message) > 0
        except:  # noqa
            logger.warning(self._logger_message(f"__send_any: error send message: {message}"))
        finally:
            self.__callback.trigger(WebSocketEventName.WEB_SOCKET_ON_SEND_MESSAGE, self, message, status)
            return status

    def send(self, message: str | bytes) -> bool:
        return self.__send_any(message)

    def send_list(self, message: list):
        return self.__send_any(message)

    def send_dict(self, message: dict):
        return self.__send_any(message)

    def get_request_id(self):
        self.__web_socket_request_id += 1
        return self.__web_socket_request_id

    def run(self, force_restart: bool = False):
        thread_to_join: Optional[threading.Thread] = None
        with self._lock_run:
            if force_restart:
                self._thread_stop_event.set()
                if not self.web_socket.closed:
                    self.web_socket.close()

                if self._thread_run_forever and self._thread_run_forever.is_alive():
                    if self._thread_run_forever != threading.current_thread():
                        thread_to_join = self._thread_run_forever

            elif self._thread_run_forever and self._thread_run_forever.is_alive():
                return

        if thread_to_join:
            thread_to_join.join(5)

        with self._lock_run:
            if self._thread_run_forever and self._thread_run_forever.is_alive():
                return

            self._thread_stop_event.clear()
            self._thread_run_forever = threading.Thread(target=self._loop_run_restart, daemon=True)
            self._thread_run_forever.start()

    def stop(self):
        thread_to_join: Optional[threading.Thread] = None
        with self._lock_run:
            self._thread_stop_event.set()
            self.web_socket.keep_running = False

            if not self.web_socket.closed:
                self.web_socket.close()

            if self._thread_run_forever and self._thread_run_forever.is_alive():
                if self._thread_run_forever != threading.current_thread():
                    thread_to_join = self._thread_run_forever

        if thread_to_join:
            thread_to_join.join(5)

        with self._lock_run:
            if self._thread_run_forever == threading.current_thread():
                self._thread_run_forever = None
            elif self._thread_run_forever and not self._thread_run_forever.is_alive():
                self._thread_run_forever = None

    def _loop_run_restart(self):
        self._thread_stop_event.clear()
        while not self._thread_stop_event.is_set():
            try:
                self._connect_count += 1
                self.__web_socket_request_id = 0
                self._run_forever()
            except Exception:  # noqa
                logger.exception(
                    self._logger_message(f"error in run_forever. Number connect = {self._connect_count}"),
                    exc_info=True
                )
                if self._thread_stop_event.wait(1):
                    return

    def _run_forever(self):
        self._api_fetch_web_socket_token()

        self.web_socket = WebSocket()

        self.web_socket.connect(
            url=WSS_URL,
            impersonate=random.choice([i.value for i in curl_cffi.BrowserType]),
            headers={"origin": BASE_URL.rstrip("/")},
            default_headers=True,
        )
        self.__on_open()

        chunks = []
        self.web_socket.keep_running = True
        sock_fd = self.web_socket.curl.getinfo(CurlInfo.ACTIVESOCKET)
        if sock_fd == CURL_SOCKET_BAD:
            raise WebSocketError("Invalid active socket", CurlECode.NO_CONNECTION_AVAILABLE)

        while self.web_socket.keep_running:
            if self._thread_stop_event.is_set():
                if not self.web_socket.closed:
                    self.web_socket.close()
                self.web_socket.keep_running = False
                break
            try:
                chunk, frame = self.web_socket.recv_fragment()
                flags = frame.flags
                self.__on_data(chunk, frame)

                chunks.append(chunk)
                if not (frame.bytesleft == 0 and flags & CurlWsFlag.CONT == 0):
                    continue

                # Concatenate collected chunks with the final message
                msg = b"".join(chunks)

                if (flags & CurlWsFlag.TEXT) and not self.web_socket.skip_utf8_validation:
                    try:
                        msg = msg.decode()  # type: ignore
                    except UnicodeDecodeError as e:
                        self.web_socket._close_code = WsCloseCode.INVALID_DATA
                        self.web_socket.close(WsCloseCode.INVALID_DATA)
                        raise WebSocketError("Invalid UTF-8", WsCloseCode.INVALID_DATA) from e

                if (flags & CurlWsFlag.BINARY) or (flags & CurlWsFlag.TEXT):
                    self.__on_message(message=msg)

                chunks = []
                if flags & CurlWsFlag.CLOSE:
                    self.web_socket.keep_running = False
                    self.__on_close(code=self.web_socket._close_code or 0, reason=self.web_socket._close_reason or "")

            except CurlError as e:
                if e.code == CurlECode.AGAIN:
                    _, _, _ = select([sock_fd], [], [], 0.5)
                else:
                    self.__on_error(exception=e)
                    if not self.web_socket.closed:
                        code = WsCloseCode.UNKNOWN
                        if isinstance(e, WebSocketError):
                            code = e.code
                        self.web_socket.close(code)
                        self.__on_close(code=self.web_socket._close_code or 0,
                                        reason=self.web_socket._close_reason or "")
                    raise

    def _selenium_get_web_socket_token(self):
        self.__web_socket_token = AuthModule().get_web_socket_token_from_selenium(self.vk_api.cookies)
        return self.__web_socket_token

    def _api_fetch_web_socket_token(self):
        user_data = self.vk_api.current_user_info()
        self.__web_socket_token = user_data.get('webSocket', {}).get('token')
        if not self.__web_socket_token:
            raise RuntimeError("Не удалось получить WebSocket token")
        return self.__web_socket_token
