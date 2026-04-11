import random
import threading
from typing import TYPE_CHECKING, Optional

from app_vkvideo.utils import DeepSeekClient, logger
from app_vkvideo.utils.deepseek_client import DeepSeekEventName
from .generator_message import MessageGenerator
from ..api.api_class import VKAPIEventName, VkapiStreamerChat, VkapiStreamerStreamInfo
from ..config import (
    CHAT_START_PAUSE,
    CHAT_INTERVAL_SEND,
    CHAT_LIMIT_MESSAGE
)
from ..web_socket.web_socket_model import (
    WebSocketEventName,
    WssStreamSlotEndChannelInfo,
    WssStreamSlotStartChannelInfo
)

if TYPE_CHECKING:
    from ..vkvideo_main import VKVideoApi


class ChatMonitor:
    def __init__(self, vk_api: "VKVideoApi", streamer_nickname: str) -> None:
        self.vk_api: VKVideoApi = vk_api
        self.streamer_nickname = streamer_nickname
        self.deepseek_client = DeepSeekClient()

        self.__req_ids = []

        self.__is_run: bool = False
        self.__thread_infinity: Optional[threading.Thread] = None
        self.__thread_stop_event = threading.Event()
        self.__lock_init_streamer = threading.Lock()

    @property
    def is_run(self) -> bool:
        return self.__is_run

    @is_run.setter
    def is_run(self, is_run: bool) -> None:
        if not isinstance(is_run, bool) or self.__is_run == is_run:
            return
        if not self.deepseek_client.enabled:
            return
        self.__is_run = is_run

        self._initialize_callback()
        if self.__is_run:
            if not self.__thread_infinity or not self.__thread_infinity.is_alive():
                self.__thread_stop_event.clear()
                self.__thread_infinity = threading.Thread(target=self.__infinity_pool_watch_chat, daemon=True)
                self.__thread_infinity.start()
        else:
            self.__thread_stop_event.set()

    def __infinity_pool_watch_chat(self) -> None:
        while self.__is_run:
            # Стартовая пауза, чтобы не писать мгновенно сообщение
            if self.__thread_stop_event.wait(
                    random.randint(CHAT_START_PAUSE[0], CHAT_START_PAUSE[1]) + random.random()
            ):
                break

            self.vk_api.get_streamer_chat(streamer_nickname=self.streamer_nickname, limit=CHAT_LIMIT_MESSAGE)

            # Интервал между запросами сообщений
            if self.__thread_stop_event.wait(CHAT_INTERVAL_SEND):
                break

    def _initialize_callback(self) -> None:
        if hasattr(self, "__init_callback"):
            return
        self.__init_callback = True

        self.vk_api.callback.register(VKAPIEventName.STREAMER_CHAT, self.__on_streamer_chat)
        self.vk_api.callback.register(VKAPIEventName.STREAMER_STREAM_INFO, self.__on_streamer_stream_info)

        self.vk_api.callback.register(DeepSeekEventName.ON_DEEPSEEK_RESPONSE, self.__on_deepseek_response)

        self.vk_api.callback.register(
            WebSocketEventName.STREAM_SLOT_START_CHANNEL_INFO, self.__on_stream_slot_start_channel_info
        )
        self.vk_api.callback.register(
            WebSocketEventName.STREAM_SLOT_END_CHANNEL_INFO, self.__on_stream_slot_end_channel_info
        )

    def __on_streamer_chat(self, streamer_id: int, user_id: int, message: VkapiStreamerChat):
        if not self.deepseek_client.enabled:
            return
        if str(user_id) != str(self.vk_api.user_id):
            return

        _streamer_nickname, _streamer_id = self.vk_api.get_streamer_data(streamer_id=streamer_id)
        if _streamer_nickname != self.streamer_nickname:
            return

        prompt_generator = MessageGenerator(class_message=message)
        active_message = prompt_generator._active_message_list()
        logger.debug(
            f"[{self.streamer_nickname}] Начинаю создавать сообщения для чата: {len(active_message)} сообщений")
        system_prompt = prompt_generator.get_system_message()
        question_prompt = prompt_generator.get_question()
        if not question_prompt or not system_prompt:
            logger.debug(f"[{self.streamer_nickname}] Не удалось создать промпты для задачи DeepSeek")
            return

        logger.debug(
            f"[{self.streamer_nickname}] отправляю задачу к DeepSeek, "
            f"размер: system={len(system_prompt)}, question={len(question_prompt)}"
        )
        req_id = self.deepseek_client.ask_in_thread(question=question_prompt, system_prompt=system_prompt)
        self.__req_ids.append(req_id)
        self.vk_api.metrics_manager.inc_metric("vkapp_gpt_requests_all")

    def __on_deepseek_response(self, request_id: str, question: str, response: str, system_prompt: str, error: str):
        if request_id not in self.__req_ids:
            return
        self.__req_ids.remove(request_id)

        if error:
            self.vk_api.metrics_manager.inc_metric("vkapp_gpt_requests_error")
        else:
            self.vk_api.metrics_manager.inc_metric("vkapp_gpt_requests_success")

        validate_text = MessageGenerator.validate_and_convert_response(response)
        if not validate_text:
            logger.debug(
                f"[{self.streamer_nickname}] ответ полученный от DeepSeek невалидный, {response}"
            )
            return

        self.vk_api.metrics_manager.inc_metric("vkapp_gpt_requests_message_current")
        logger.debug(f"[{self.streamer_nickname}] предложенное сообщение от DeepSeek\n{response}")
        self.vk_api.send_message_chat(self.streamer_nickname, validate_text)

    def __on_streamer_stream_info(
            self, streamer_id: int, user_id: int, message: VkapiStreamerStreamInfo
    ):
        if str(user_id) != str(self.vk_api.user_id):
            return
        _streamer_nickname, _streamer_id = self.vk_api.get_streamer_data(streamer_id=streamer_id)
        if _streamer_nickname != self.streamer_nickname:
            return

        if not message.data.stream.is_online:
            self.is_run = False

    def __on_stream_slot_start_channel_info(
            self, streamer_id: int, user_id: int, message: WssStreamSlotStartChannelInfo
    ):
        _streamer_nickname, _streamer_id = self.vk_api.get_streamer_data(streamer_id=streamer_id)
        if _streamer_nickname != self.streamer_nickname:
            return

        self.is_run = True

    def __on_stream_slot_end_channel_info(
            self, streamer_id: int, user_id: int, message: WssStreamSlotEndChannelInfo
    ):
        _streamer_nickname, _streamer_id = self.vk_api.get_streamer_data(streamer_id=streamer_id)
        if _streamer_nickname != self.streamer_nickname:
            return

        self.is_run = False
