from peewee import ForeignKeyField, BooleanField, CharField, TextField
from .account import Account
from ._base_model import BaseModel

class Settings(BaseModel):
    account = ForeignKeyField(Account, backref='settings', unique=True)
    theme = CharField(default='light')  # light/dark
    language = CharField(default='ru')
    notifications_enabled = BooleanField(default=True)
    auto_download = BooleanField(default=False)
    download_path = TextField(default='')
