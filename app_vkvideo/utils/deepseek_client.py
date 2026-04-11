import argparse
import sys
import threading
import uuid
from enum import Enum

from openai import APIConnectionError, OpenAI, RateLimitError
from openai.types.chat import ChatCompletionSystemMessageParam, ChatCompletionUserMessageParam

from app_vkvideo.config import Config
from .callback_manager import CallbackManager
from .logging_setup import logger


class DeepSeekEventName(Enum):
    ON_DEEPSEEK_RESPONSE = "on_deepseek_response"


class DeepSeekClient:
    """Потокобезопасный Singleton-клиент для работы с DeepSeek API."""

    _instance: "DeepSeekClient" = None
    _new_lock = threading.Lock()
    _init_lock = threading.Lock()

    def __new__(cls, api_key: str | None = None, *args,
                **kwargs) -> "DeepSeekClient":  # pylint: disable=unused-argument
        if cls._instance is None:
            with cls._new_lock:
                if cls._instance is None:
                    instance = super().__new__(cls)
                    instance._init_lock = cls._init_lock
                    cls._instance = instance
        return cls._instance

    def __init__(self, api_key: str | None = None, timeout: int = 60):
        if not hasattr(self, "_init_lock"):
            self._init_lock = DeepSeekClient._init_lock

        with self._init_lock:
            if getattr(self, "_initialized", None) is not None:
                return
            api_key = api_key or self._get_api_key_from_cli()

            self.api_key = api_key
            self.model = Config.DEEPSEEK_MODEL
            self.timeout = timeout
            self.base_url = Config.DEEPSEEK_BASE_URL
            self.callback_manager = CallbackManager()
            self.client = None
            self.enabled = bool(self.api_key)
            if self.enabled:
                self.client = OpenAI(
                    api_key=self.api_key,
                    base_url=self.base_url,
                    timeout=self.timeout,
                )
            else:
                logger.warning("DeepSeek disabled: API key was not provided")
            self._initialized = True

    @staticmethod
    def _get_api_key_from_cli() -> str:
        parser = argparse.ArgumentParser(add_help=False)
        parser.add_argument("--deepseek-api-key", default="")
        args, _ = parser.parse_known_args(sys.argv[1:])
        return (args.deepseek_api_key or "").strip()

    def ask(self, question: str, system_prompt: str | None = None) -> str:
        """Отправляет вопрос в DeepSeek и возвращает текст ответа."""
        if not question or not question.strip():
            raise ValueError("Question must not be empty")
        if not self.enabled or self.client is None:
            logger.debug("DeepSeek request skipped: client is disabled")
            return ""

        messages: list = []
        if system_prompt:
            messages.append(ChatCompletionSystemMessageParam(role="system", content=system_prompt))
        messages.append(ChatCompletionUserMessageParam(role="user", content=question.strip()))

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
            )
        except APIConnectionError as exc:
            logger.exception("DeepSeek API connection error")
            raise RuntimeError(f"DeepSeek API connection error: {exc}") from exc
        except RateLimitError as exc:
            logger.exception("DeepSeek API rate limit error")
            raise RuntimeError(f"DeepSeek API rate limit error: {exc}") from exc
        except Exception as exc:  # noqa
            logger.exception("DeepSeek API request failed")
            raise RuntimeError(f"DeepSeek API request failed: {exc}") from exc

        choices = response.choices or []
        if not choices:
            raise RuntimeError("DeepSeek API returned no choices")

        message = choices[0].message
        content = message.content
        if not content:
            raise RuntimeError("DeepSeek API returned empty content")

        return content.strip()

    def ask_in_thread(self, question: str, system_prompt: str | None = None) -> str:
        """Запускает запрос в отдельном потоке и рассылает результат через CallbackManager."""

        def _run(_request_id: str) -> None:
            try:
                response = self.ask(question=question, system_prompt=system_prompt)
                self.callback_manager.trigger(
                    DeepSeekEventName.ON_DEEPSEEK_RESPONSE,
                    request_id=_request_id,
                    question=question,
                    response=response,
                    system_prompt=system_prompt,
                    error=None,
                )
            except Exception as exc:  # noqa
                logger.exception("DeepSeek threaded request failed")
                self.callback_manager.trigger(
                    DeepSeekEventName.ON_DEEPSEEK_RESPONSE,
                    request_id=_request_id,
                    question=question,
                    response="",
                    system_prompt=system_prompt,
                    error=str(exc),
                )

        request_id = str(uuid.uuid4())
        threading.Thread(target=_run, args=(request_id,), daemon=True).start()
        return request_id
