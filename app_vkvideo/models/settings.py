from typing import Optional, Any

from peewee import TextField, IntegerField, BooleanField

from app_vkvideo.utils import decrypt_text, encrypt_text
from ._base_model import BaseModel


class Setting(BaseModel):
    id = IntegerField(primary_key=True)
    key = TextField(unique=True)
    value = TextField(default='', null=True)
    is_cripted = BooleanField(default=False, null=True)

    @classmethod
    def get_or_create_setting(cls, key_name: str = "") -> Optional["Setting"]:
        if not key_name:
            return None
        model, _ = cls.get_or_create(key=key_name)
        return model

    @property
    def value_decrypted(self) -> TextField | str:
        if not self.is_cripted:
            return self.value
        return decrypt_text(self.value)

    @value_decrypted.setter
    def value_decrypted(self, value: Any) -> None:
        self.value = encrypt_text(value)
        self.is_cripted = True

    @classmethod
    def set_value(cls, key: str, value: str, encrypted: bool = False) -> Optional["Setting"]:
        setting = cls.get_or_create_setting(key)
        if not setting:
            return None

        if encrypted:
            setting.value_decrypted = value
        else:
            setting.value = value
            setting.is_cripted = False

        setting.save()
        return setting

    def __str__(self):
        return f"Setting(key={self.key}, is_cripted={self.is_cripted}, value={self.value})"
