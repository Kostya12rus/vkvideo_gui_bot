import webbrowser

import psutil

from .logging_setup import logger


def kill_process_tree(pid: int, timeout: float = 3.0):
    """Принудительно завершает процесс и всех его потомков, дожидаясь их завершения.

    Args:
        pid (int): PID процесса.
        timeout (float, optional): Время ожидания завершения потомков в секундах.
    """
    try:
        if not psutil.pid_exists(pid):
            return
        parent = psutil.Process(pid)

        children = parent.children(recursive=True)
        for proc in children:
            try:
                proc.terminate()
            except psutil.NoSuchProcess:
                continue

        try:
            parent.terminate()
        except psutil.NoSuchProcess:
            return

        _, alive = psutil.wait_procs(children + [parent], timeout=timeout)
        for proc in alive:
            try:
                proc.kill()
            except psutil.NoSuchProcess:
                continue
        psutil.wait_procs(alive, timeout=timeout)
    except Exception:  # noqa
        logger.exception(f"Ошибка при завершении дерева процессов с PID={pid}", exc_info=True)


def open_url(url: str = ""):
    if not url:
        return
    webbrowser.open(url)
