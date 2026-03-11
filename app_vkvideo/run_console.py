import argparse
import socket
import time

from loguru import logger

from app_vkvideo.models import init_db, Account
from app_vkvideo.vkvideo_api import VKVideoApi
from monitoring import MetricsManager


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Запуск VKVideo бота в консольном режиме")
    parser.add_argument(
        "--metrics-host",
        default="localhost",
        help="Хост Pushgateway для отправки метрик (по умолчанию: localhost)",
    )
    parser.add_argument(
        "--metrics-port",
        type=int,
        default=9091,
        help="Порт Pushgateway для отправки метрик (по умолчанию: 9091)",
    )
    parser.add_argument(
        "--metrics-interval",
        type=float,
        default=5.0,
        help="Интервал фонового сбора ресурсных метрик в секундах (по умолчанию: 5.0)",
    )
    parser.add_argument(
        "--is-debug",
        type=bool,
        default=False,
        help="Дебаг режим",
    )
    return parser.parse_args()

def create_metrics(user_id: int|str) -> MetricsManager:
    args = parse_args()
    return MetricsManager(
        host=args.metrics_host,
        port=args.metrics_port,
        user_id=str(user_id),
        hostname=socket.gethostname(),
        collect_interval=args.metrics_interval,
        autostart=True,
    )


def run():
    args = parse_args()

    init_db()
    accounts = Account.get_all()
    if not accounts:
        logger.info("У вас нет сохраненных аккаунтов. Авторизуемся?")
        new_user = VKVideoApi.start_auth()

        user_info = new_user.actor_info()
        account_id = user_info['data']["actor"]["id"]
        user_nickname = user_info['data']["actor"]['nick']

        account = Account.get_or_create_account(account_id)
        account.nickname = user_nickname
        account.cookies_decrypted = new_user.cookies
        account.save()
    else:
        logger.info("Найден сохраненный аккаунт.")
        account: Account = accounts[0]
        new_user = VKVideoApi(account.account_id, account.cookies_decrypted)

        logger.info("Перед запуском бота обновляю авторизационные данные")
        new_user = new_user.refresh_auth()

    new_user.metrics_manager = create_metrics(new_user.user_id)

    new_user.wss_api.is_debug = args.is_debug
    logger.info("Запускаю просмотр за стримерами на которые вы подписаны и сейчас онлайн")
    new_user.start_watch_online_subscribers()
    logger.info("Запускаю просмотр за стримерами у которые включена Бокс Компания")
    new_user.start_watch_drop_streamers()

    while True:
        time.sleep(1)


if __name__ == "__main__":
    run()
