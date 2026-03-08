import random
import threading
import time
import uuid
from typing import TYPE_CHECKING
from loguru import logger

from ..config import USER_HEARTBEAT_VIEWER_URL, BASE_URL

if TYPE_CHECKING:
    from ..vkvideo_main import VKVideoApi


class HeartbeatApi:
    def __init__(self, vk_api: "VKVideoApi", streamer_nickname: str):
        self.vk_api = vk_api
        self.streamer_nickname = streamer_nickname
        self.__stream_id = ""
        self.__is_run = None
        self.__is_online = None
        self.__thread = threading.Thread(target=self.__infinity_pool_watch_stream, daemon=True)

    @property
    def is_run(self) -> bool:
        return self.__is_run

    @is_run.setter
    def is_run(self, is_run: bool) -> None:
        if not isinstance(is_run, bool) or self.__is_run == is_run:
            return
        self.__stream_id = ""
        self.__is_run = is_run
        self.__is_online = False

        if not self.__thread.is_alive():
            self.__thread = threading.Thread(target=self.__infinity_pool_watch_stream, daemon=True)
            self.__thread.start()

    def __infinity_pool_watch_stream(self) -> None:
        while True:
            if not self.__is_run:
                return
            if not self.__is_online or not self.__stream_id:
                streamer_info = self.vk_api.get_streamer_stream_info(self.streamer_nickname)
                self.__is_online = streamer_info.data.stream.is_online
                self.__stream_id = streamer_info.data.stream.id
                if not self.__is_online or not self.__stream_id:
                    time_sleep = 60 + random.randint(0, 10) + random.random()
                    time.sleep(time_sleep)
                    continue

            next_send_heartbeat_sec = self.__send_heartbeat_viewer()
            if not isinstance(next_send_heartbeat_sec, (int, float)):
                time.sleep(5)
                continue

            time.sleep(next_send_heartbeat_sec)

    def __send_heartbeat_viewer(self, send_type: str = "") -> int | float | None:
        req = self.vk_api.request(
            USER_HEARTBEAT_VIEWER_URL.format(self.streamer_nickname, self.__stream_id) + send_type,
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
                f"Поток просмотра стримера '{self.streamer_nickname}' помер, статус ответа '{req.status_code}'"
            )
            self.__is_online = False
            return None
        elif not req.ok:
            logger.error(
                f"Поток просмотра стримера '{self.streamer_nickname}' помер, статус ответа '{req.status_code}'"
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