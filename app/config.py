import os
import pathlib


class Config:
    MAIN_PATH = pathlib.Path(os.getcwd()).absolute()
    DATA_PATH = MAIN_PATH / "data"
    DATABASE_PATH = DATA_PATH / "database.sqlite3"
    DEBUG = True
