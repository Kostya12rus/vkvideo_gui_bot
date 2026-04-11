import os
import pathlib


class Config:
    MAIN_PATH = pathlib.Path(os.getcwd()).absolute()
    DATA_PATH = MAIN_PATH / "data"
    DATABASE_PATH = DATA_PATH / "database.sqlite3"
    DEBUG = True
    DEEPSEEK_BASE_URL = "https://api.deepseek.com"
    DEEPSEEK_MODEL = "deepseek-reasoner"
