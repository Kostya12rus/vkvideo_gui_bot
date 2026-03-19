import argparse
import socket
import time
from typing import Any

from loguru import logger

from app_vkvideo.models import init_db, Account
from app_vkvideo.vkvideo_api import VKVideoApi
from app_vkvideo.monitoring import MetricsManager


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
        "--hostname",
        default="",
        help="",
    )
    parser.add_argument(
        "--is-debug",
        action="store_true",
        help="Включить дебаг режим WebSocket",
    )
    parser.add_argument(
        "--disable-farm-drop-company",
        action="store_true",
        help='Не смотреть стримеров участвующих в Бокс-кампаниях',
    )
    parser.add_argument(
        "--farm-catalog-id",
        default="",
        help='Просмотр стримеров в указанной категории (по умолчанию: "")',
    )
    return parser.parse_args()


def create_metrics(user_id: int | str, args: argparse.Namespace) -> Any:
    hostname = args.hostname if args.hostname else socket.gethostname()
    return MetricsManager(
        host=args.metrics_host,
        port=args.metrics_port,
        user_id=str(user_id),
        hostname=hostname,
        collect_interval=args.metrics_interval,
        autostart=True,
    )


def run():
    args = parse_args()
    logger.info("Запущена консольная версия от 19.03.2026 22:11")

    init_db()
    accounts = Account.get_all()
    if not accounts:
        logger.info("У вас нет сохраненных аккаунтов. Пожалуйста авторизуйтесь, открываю браузер...")
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

    new_user.metrics_manager = create_metrics(new_user.user_id, args)

    web_socket_api = getattr(new_user, "web_socket_api", None)
    if web_socket_api is not None:
        web_socket_api.is_debug = args.is_debug
    logger.info("Запускаю просмотр стримеров на которые подписан аккаунт и сейчас онлайн")
    new_user.start_watch_online_subscribers()
    if not args.disable_farm_drop_company:
        logger.info("Запускаю просмотр стримеров у которые участвуют в Бокс-кампаниях")
        new_user.start_watch_drop_streamers()
    if args.farm_catalog_id:
        logger.info(f"Запускаю просмотр стримеров из категории '{args.farm_catalog_id}'")
        new_user.start_watch_catalog_streamers(args.farm_catalog_id)

    while True:
        time.sleep(1)


if __name__ == "__main__":
    run()
