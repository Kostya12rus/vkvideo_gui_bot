from ._base_model import db
from .account import Account


def init_db() -> None:
    """Инициализация базы данных."""
    db.connect()
    db.create_tables(
        [
            Account,
        ]
    )


__all__ = [
    "Account",
    "db",
    "init_db"
]
