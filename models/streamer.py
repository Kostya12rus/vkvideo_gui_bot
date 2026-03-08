from peewee import CharField, IntegerField, DateTimeField

from ._base_model import BaseModel


class Streamer(BaseModel):
    streamer_id = IntegerField(unique=True)
    username = CharField()
    display_name = CharField()
    platform = CharField()  # например, 'vkvideo'
    created_at = DateTimeField()
    updated_at = DateTimeField()
