from ._base_model import db
from .account import Account
from .settings import Setting


def init_db() -> None:
    """Инициализация базы данных."""
    db.connect()
    db.create_tables(
        [
            Account,
            Setting
        ]
    )


__all__ = [
    "Account", "Setting",
    "db",
    "init_db"
]
