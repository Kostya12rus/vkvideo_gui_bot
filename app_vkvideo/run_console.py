import time

from loguru import logger

from .models import init_db, Account
from .vkvideo_api import VKVideoApi


def run():
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

    new_user.wss_api.is_debug = True
    logger.info("Запускаю просмотр за стримерами на которые вы подписаны")
    new_user.start_watch_all_subscribers()
    logger.info("Запускаю просмотр за стримерами у которые включена Бокс Компания")
    new_user.start_watch_drop_streamers()

    while True:
        time.sleep(1)


if __name__ == "__main__":
    run()
