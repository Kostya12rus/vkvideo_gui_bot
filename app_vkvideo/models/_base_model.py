# pylint: skip-file
import pathlib

from peewee import Model, SqliteDatabase

from app_vkvideo.config import Config

db_path = pathlib.Path(Config.DATABASE_PATH)
db_path.parent.mkdir(parents=True, exist_ok=True)
db = SqliteDatabase(db_path.absolute().as_posix())


class BaseModel(Model):
    class Meta:
        database = db
