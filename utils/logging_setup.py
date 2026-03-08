import pathlib
import sys
import time

from loguru import logger

logger.remove()

logs_folder = pathlib.Path("_logs")
logs_folder.mkdir(parents=True, exist_ok=True)
time_log = time.strftime("%Y-%m-%d")  # _%H-%M-%S

FORMAT_LOG = (
    "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}:{function}:{line}</cyan> - <b>{message}</b>"
)

logger.add(
    logs_folder / f'{time_log}_logs.log',
    format=FORMAT_LOG,
    level="INFO",
    enqueue=True,
    rotation="1 MB",
    filter=lambda record: record["level"].name == "INFO"
)
logger.add(
    logs_folder / f'{time_log}_exceptions.log',
    level="ERROR",
    backtrace=True,
    diagnose=True,
    enqueue=True,
    rotation="1 MB",
    filter=lambda record: record["level"].name == "ERROR"
)

if sys.stdout:
    logger.add(
        sys.stdout,
        format=FORMAT_LOG,
        level="INFO",
        filter=lambda record: record["level"].name == "INFO"
    )
    logger.add(
        sys.stdout,
        format=FORMAT_LOG,
        level="DEBUG",
        filter=lambda record: record["level"].name == "DEBUG"
    )
    logger.add(
        sys.stdout,
        format=FORMAT_LOG,
        level="ERROR",
        filter=lambda record: record["level"].name == "ERROR"
    )

    logger.add(
        logs_folder / f'{time_log}_debug.log',
        format=FORMAT_LOG,
        level="DEBUG",
        enqueue=True,
        rotation="100 MB",
        filter=lambda record: record["level"].name == "DEBUG"
    )
    logger.info(f'Логи будут хранится в папке: {logs_folder.absolute()}')
