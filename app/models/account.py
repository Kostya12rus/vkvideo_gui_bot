from typing import Optional, Any

from peewee import CharField, IntegerField

from app.utils import decrypt_text, encrypt_text
from ._base_model import BaseModel


class Account(BaseModel):
    account_id = IntegerField(unique=True)
    nickname = CharField(null=True)
    cookies = CharField(null=True)

    @classmethod
    def get_or_create_account(cls, account_id: Optional[int] = None) -> Optional["Account"]:
        if not isinstance(account_id, int) or not account_id:
            return None
        model, _ = cls.get_or_create(account_id=account_id)
        return model

    @classmethod
    def get_all(cls) -> list["Account"]:
        return [account for account in cls.select()]

    @property
    def cookies_decrypted(self) -> list[dict[str, Any]]:
        return decrypt_text(self.cookies)

    @cookies_decrypted.setter
    def cookies_decrypted(self, value: list[dict[str, Any]]) -> None:
        self.cookies = encrypt_text(value)

    def __str__(self): return f"Account(account_id={self.account_id}, nickname={self.nickname})"

    def __repr__(self): return self.__str__()
