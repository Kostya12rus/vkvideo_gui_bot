from peewee import ForeignKeyField, DateTimeField

from ._base_model import BaseModel
from .account import Account
from .streamer import Streamer


class Subscription(BaseModel):
    account = ForeignKeyField(Account, backref='subscriptions')
    streamer = ForeignKeyField(Streamer, backref='subscribers')
    subscribed_at = DateTimeField()

    class Meta:
        indexes = (
            (('account', 'streamer'), True),  # уникальная пара
        )
