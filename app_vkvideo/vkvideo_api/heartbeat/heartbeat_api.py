import random
import threading
import uuid
from typing import TYPE_CHECKING, Optional

from loguru import logger

from ..web_socket.web_socket_model import *
from ..api.api_class import *
from ..config import USER_HEARTBEAT_VIEWER_URL, BASE_URL

if TYPE_CHECKING:
    from ..vkvideo_main import VKVideoApi


class HeartbeatApi:
    def __init__(self, vk_api: "VKVideoApi", streamer_nickname: str):
        self.vk_api = vk_api
        self.user_id = vk_api.user_id
        self.streamer_nickname = streamer_nickname
        self.streamer_id: Optional[int] = None
        self.streamer_stream_id: str = ""
        self.streamer_is_online: bool = False

        self._last_streamer_info: Optional[VkapiStreamerInfo] = None
        self._last_streamer_stream_info: Optional[VkapiStreamerStreamInfo] = None
        self._last_channel_stream_channel_info: Optional[WssChannelStreamChannelInfo] = None

        self.__callback = self.vk_api.callback

        self.__is_run: bool = False
        self.__thread_watch_stream: Optional[threading.Thread] = None
        self.__thread_stop_event = threading.Event()
        self.__lock_init_streamer = threading.Lock()

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
            if not self.__thread_watch_stream or not self.__thread_watch_stream.is_alive():
                self.__thread_stop_event.clear()
                self.__thread_watch_stream = threading.Thread(target=self.__infinity_pool_watch_stream, daemon=True)
                self.__thread_watch_stream.start()
        else:
            self.__thread_stop_event.set()

    def __infinity_pool_watch_stream(self) -> None:
        try_fetch_streamer_info = 0
        while self.__is_run:
            if not self._last_streamer_info or not self._last_streamer_stream_info:
                try_fetch_streamer_info += 1
                if try_fetch_streamer_info > 10:
                    logger.info(
                        f"[{self.streamer_nickname}] Не удалось получить информацию о стримере за 10 попыток. "
                        f"Отключаю..."
                    )
                    break
                self.__init_streamer_info()
                # threading.Thread(target=self.__init_streamer_info, daemon=True).start()

            if not self.streamer_is_online or not self.streamer_stream_id:
                if self.__thread_stop_event.wait(random.randint(5, 10) + random.random()):
                    break
                continue

            next_send_heartbeat_sec = self.__send_heartbeat_viewer()
            if not isinstance(next_send_heartbeat_sec, (int, float)):
                if self.__thread_stop_event.wait(random.randint(5, 10) + random.random()):
                    break
                continue

            if self.__thread_stop_event.wait(next_send_heartbeat_sec):
                break

    def __init_streamer_info(self) -> None:
        with self.__lock_init_streamer:
            if self._last_streamer_info and self._last_streamer_stream_info:
                return

            logger.debug(f"[{self.streamer_nickname}] Делаю подгрузку информации о стримере и его стриме")
            streamer_info = self.vk_api.get_streamer_info(self.streamer_nickname)
            streamer_stream_info = self.vk_api.get_streamer_stream_info(self.streamer_nickname)

            streamer_nickname = streamer_info.blog_url
            streamer_id = streamer_info.owner.id
            streamer_stream_id = streamer_stream_info.data.stream.id
            streamer_is_online = streamer_stream_info.data.stream.is_online
            if streamer_id:
                self._last_streamer_info = streamer_info
            if streamer_stream_id:
                self._last_streamer_stream_info = streamer_stream_info

            logger.debug(
                f"[{self.streamer_nickname}] Подгрузка информации завершена: "
                f"{self.user_id=}, {streamer_nickname=}, {streamer_id=}, {streamer_stream_id=}, {streamer_is_online=}"
            )
            self.update_streamer_stream_info(
                user_id=self.user_id,
                streamer_nickname=streamer_nickname,
                streamer_id=streamer_id,
                streamer_stream_id=streamer_stream_id,
                streamer_is_online=streamer_is_online,
            )

            self.__thread_stop_event.wait(random.randint(5, 10) + random.random())

    def __send_heartbeat_viewer(self, send_type: str = "") -> int | float | None:
        try:
            req = self.vk_api.request(
                USER_HEARTBEAT_VIEWER_URL.format(self.streamer_nickname, self.streamer_stream_id) + send_type,
                "PUT",
                headers={
                    "Accept": "application/json, text/plain, */*",
                    "accept-encoding": "gzip, deflate, br, zstd",
                    "accept-language": "ru,en;q=0.9",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "origin": BASE_URL,
                    "referer": f"{BASE_URL}/{self.streamer_nickname}",
                    "x-app": "streams_web",
                    "x-from-id": str(uuid.uuid4()),
                }
            )

            if req.status_code == 404:
                logger.error(
                    f"{self.user_id}: '{self.streamer_nickname}'[{self.streamer_id}] "
                    f"Поток просмотра стримера помер, статус ответа '{req.status_code}'"
                )
                self.streamer_is_online = False
                self.streamer_stream_id = ""
                return None
            elif not req.ok:
                logger.error(
                    f"{self.user_id}: '{self.streamer_nickname}'[{self.streamer_id}] "
                    f"Поток просмотра стримера помер, статус ответа '{req.status_code}'"
                )
                return None

            req_json = req.json()
            interval = req_json.get('data', {}).get('nextRequestInterval')
            if not isinstance(interval, (int, float)):
                logger.error(
                    f"Поток просмотра стримера '{self.streamer_nickname}' не вернул интервал времени, "
                    f"статус ответа '{req.status_code}', полученый ответ '{req_json}'"
                )
                return None

            return interval
        except Exception as e:  # noqa
            logger.error(
                f"[{self.streamer_nickname}]: Не удалось пингануть о просмотре стрима"
            )
            return None

    def update_streamer_stream_info(
            self,
            user_id: int, streamer_nickname: str, streamer_id: int, streamer_stream_id: str, streamer_is_online: bool,
            is_run: Optional[bool] = None
    ) -> None:
        if str(self.user_id) != str(user_id):
            return
        if str(self.streamer_nickname).lower() != str(streamer_nickname).lower():
            return

        if str(self.streamer_id) != str(streamer_id):
            self.streamer_id = streamer_id
        if str(self.streamer_stream_id) != str(streamer_stream_id):
            self.streamer_stream_id = streamer_stream_id
        if self.streamer_is_online != str(streamer_stream_id):
            self.streamer_is_online = streamer_is_online

        if is_run is not None:
            self.is_run = is_run

    def _initialize_callback(self) -> None:
        if hasattr(self, "__init_callback"):
            return
        self.__init_callback = True
        self.__callback.register(VKAPIEventName.STREAMER_INFO, self.__on_streamer_info)
        self.__callback.register(VKAPIEventName.STREAMER_STREAM_INFO, self.__on_streamer_stream_info)

        self.__callback.register(WebSocketEventName.CHANNEL_STREAM_CHANNEL_INFO, self.__channel_stream_channel_info)
        self.__callback.register(WebSocketEventName.STREAM_SLOT_START_CHANNEL_INFO, self.__on_stream_slot_start_channel_info)
        self.__callback.register(WebSocketEventName.STREAM_SLOT_END_CHANNEL_INFO, self.__on_stream_slot_end_channel_info)

    def __on_streamer_info(self, streamer_id: int, user_id: int, message: VkapiStreamerInfo):
        streamer_nickname = message.blog_url
        if not streamer_nickname or str(streamer_nickname).lower() != str(self.streamer_nickname).lower():
            return
        self.streamer_id = message.owner.id

        if self.streamer_id:
            self._last_streamer_info = message

    def __on_streamer_stream_info(self, streamer_id: int, user_id: int, message: VkapiStreamerStreamInfo):
        streamer_nickname = message.data.stream.embed_url.split("/")[-1]
        if str(streamer_nickname) != str(self.streamer_nickname):
            return
        self.streamer_id = message.data.stream.user.id
        self.streamer_is_online = message.data.stream.is_online
        self.streamer_stream_id = message.data.stream.id

        if self.streamer_stream_id:
            self._last_streamer_stream_info = message

    def __channel_stream_channel_info(self, streamer_id: int, user_id: int, message: WssChannelStreamChannelInfo):
        if not streamer_id or str(streamer_id) != str(self.streamer_id):
            return
        data = message.push.pub.data.data
        self.streamer_is_online = data.stream.is_online
        self.streamer_stream_id = data.stream.id
        if self.streamer_stream_id:
            self._last_channel_stream_channel_info = message

    def __on_stream_slot_start_channel_info(self, streamer_id: int, user_id: int, message: WssStreamSlotStartChannelInfo):
        if not streamer_id or str(streamer_id) != str(self.streamer_id):
            return
        self.streamer_is_online = True

    def __on_stream_slot_end_channel_info(self, streamer_id: int, user_id: int, message: WssStreamSlotEndChannelInfo):
        if not streamer_id or str(streamer_id) != str(self.streamer_id):
            return
        self.streamer_is_online = False
