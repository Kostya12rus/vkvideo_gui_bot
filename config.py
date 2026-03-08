import pathlib


class Config:
    DATABASE_PATH = pathlib.Path("data/database.sqlite3")
    DEBUG = True
