import asyncio
import inspect
import threading
import weakref
from enum import Enum
from types import MethodType
from typing import Union, Callable, Any

from .logging_setup import logger


class EventName(Enum):
    ON_SET_SNACK_BAR_TEST = "on_set_snack_bar_test"


class CallbackManager:
    """Менеджер событий и колбэков (реализация паттерна 'Observer' с потокобезопасностью).

    Реализует паттерн Singleton с потокобезопасными операциями. Позволяет регистрировать,
    удалять и асинхронно вызывать обработчики событий с автоматическим логированием ошибок.

    Attributes:
        _instance (CallbackManager): Единственный экземпляр класса
        _new_lock (threading.Lock): Блокировка для потокобезопасности операций __new__
        _init_lock (threading.Lock): Блокировка для потокобезопасности операций __init__
        _lock (threading.Lock): Блокировка для потокобезопасности операций
        _callbacks (dict): Словарь колбэков в формате {event_name: [weakref]}
        _thread_semaphore (threading.Semaphore): Семафор для контроля количества потоков
        _ref_to_event (dict): Словарь ссылок на колбэки в формате {ref: (event_name, weakref)}
    """
    _instance: "CallbackManager" = None
    _new_lock = threading.Lock()
    _init_lock = threading.Lock()

    def __new__(cls, *args, **kwargs) -> 'CallbackManager':  # pylint: disable=unused-argument
        if cls._instance is None:
            with cls._new_lock:
                if cls._instance is None:
                    instance = super().__new__(cls)
                    instance._init_lock = cls._init_lock
                    cls._instance = instance
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_init_lock'):
            self._init_lock = CallbackManager._init_lock

        with self._init_lock:
            if hasattr(self, "_initialized"):
                return

            self._lock = threading.Lock()
            self._callbacks = {}  # {event_name: [weakref]}
            self._thread_semaphore = threading.Semaphore(10)
            self._ref_to_event = {}  # {ref: (event_name, weakref)}
            self._initialized = True  # Флаг, что init уже выполнен

    def _make_weakref(self, event_name: Union[EventName, str], callback: Callable) -> Callable:
        """Создаёт weakref и регистрирует автоудаление

        Args:
            event_name (Union[EventName, str]): Название события.
            callback (Callable): Функция, которую нужно удалить.
        """
        if isinstance(callback, MethodType):
            ref = weakref.WeakMethod(callback, self._auto_remove)
        else:
            ref = weakref.ref(callback, self._auto_remove)

        self._ref_to_event[ref] = (event_name, ref)
        return ref

    def _auto_remove(self, ref: Any):
        """Вызывается автоматически при сборке мусора объекта, связанного с колбэком

        Args:
            ref (Any): Ссылка на колбэк
        """
        with self._lock:
            event_info = self._ref_to_event.pop(ref, None)
            if not event_info:
                return
            event_name, _ = event_info
            if event_name in self._callbacks:
                self._callbacks[event_name] = [r for r in self._callbacks[event_name] if r is not ref]
                if not self._callbacks[event_name]:
                    del self._callbacks[event_name]

    def register(self, event_name: Union[EventName, str], callback: Callable) -> None:
        """Регистрирует колбэк на событие.

        Args:
            event_name (Union[EventName, str]): Название события.
            callback (Callable): Функция, вызываемая при возникновении события.
        """
        with self._lock:
            self._callbacks.setdefault(event_name, [])
            ref = self._make_weakref(event_name, callback)
            if ref not in self._callbacks[event_name]:
                self._callbacks[event_name].append(ref)

    def unregister(self, event_name: Union[EventName, str], callback: Callable) -> None:
        """Удаляет зарегистрированный колбэк с события.

        Args:
            event_name (Union[EventName, str]): Название события.
            callback (Callable): Функция, которую нужно удалить.
        """
        with self._lock:
            if event_name in self._callbacks:
                ref_to_remove = self._make_weakref(event_name, callback)
                self._callbacks[event_name] = [ref for ref in self._callbacks[event_name] if ref != ref_to_remove]
                if not self._callbacks[event_name]:
                    del self._callbacks[event_name]

    def trigger(self, event_name: Union[EventName, str], *args, **kwargs) -> None:
        """Вызывает все зарегистрированные колбэки для события в отдельных потоках.

        Args:
            event_name (Union[EventName, str]): Название события.
            *args: Позиционные аргументы, передаваемые в колбэк.
            **kwargs: Именованные аргументы, передаваемые в колбэк.
        """
        with self._lock:
            callback_refs = list(self._callbacks.get(event_name, []))

        for ref in callback_refs:
            threading.Thread(
                target=self._run_with_semaphore,
                args=args,
                kwargs={**kwargs, 'callback': ref}
            ).start()

    def _run_with_semaphore(self, *args, callback: Callable = None, **kwargs) -> None:
        """Вызывает колбэк в потоке с блокировкой потокобезопасности.

        Args:
            callback (Callable, optional): Колбэк, который требуется вызвать.
            *args: Позиционные аргументы, передаваемые в колбэк.
            **kwargs: Именованные аргументы, передаваемые в колбэк.
        """
        with self._thread_semaphore:
            real_callback = callback()
            if callback is None:
                return

            self.__callback_errors(*args, callback=real_callback, **kwargs)

    def __callback_errors(self, *args, callback: Callable = None, **kwargs) -> None:
        """Вызывает указанный колбэк с передачей аргументов и обработкой исключений.

        Args:
            *args: Позиционные аргументы, передаваемые в колбэк.
            callback (Callable, optional): Колбэк, который требуется вызвать.
            **kwargs: Именованные аргументы, передаваемые в колбэк.
        """
        try:
            if inspect.iscoroutinefunction(callback):
                asyncio.run(self.__run_async(callback, *args, **kwargs))
            else:
                callback(*args, **kwargs)
        except Exception:  # noqa
            logger.exception(f"Ошибка при вызове callback: {callback}")

    @staticmethod
    async def __run_async(callback, *args, **kwargs):
        try:
            await callback(*args, **kwargs)
        except Exception:  # noqa
            logger.exception(f"[async] Ошибка при вызове callback: {callback}")

    def get_registered_callbacks(self, event_name: Union[EventName, str]) -> list[str]:
        """Возвращает список строковых представлений зарегистрированных колбэков (для отладки)

        Args:
            event_name (Union[EventName, str]): Название события

        Returns:
            list[str]: Список строковых представлений
        """
        with self._lock:
            refs = self._callbacks.get(event_name, [])
            return [f"{ref().__module__}.{ref().__name__}" if ref() else "<dead callback>" for ref in refs]

    def dispose(self):
        """ Очищает менеджер колбэков. """
        with self._lock:
            self._callbacks.clear()
            self._ref_to_event.clear()
