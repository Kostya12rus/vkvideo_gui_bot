import functools
import threading
from typing import Callable, Optional, Any

from .logging_setup import logger


def run_in_thread(func: Callable[..., bool]) -> Callable[..., Optional[Any]]:
    """
    Декоратор для запуска метода в отдельном потоке.

    Метод должен принимать параметр blocking: bool = False в своей сигнатуре,
    но декоратор не передаёт его в сам метод, а только использует для ожидания.

    Returns:
        Значение функции bool или str, если blocking=True.
        None, если blocking=False.
    """

    @functools.wraps(func)
    def wrapper(self, *args, **kwargs) -> Optional[Any]:
        blocking = kwargs.pop("blocking", False)
        result = {}

        def _run():
            try:
                result["value"] = func(self, *args, **kwargs)
            except Exception as e:  # noqa
                logger.exception("Ошибка при выполнении функции в отдельном потоке")
                result["error"] = str(e)

        thread = threading.Thread(target=_run, daemon=True)
        thread.start()

        if blocking:
            thread.join()
            return result.get("value", False)
        return None

    return wrapper
