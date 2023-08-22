__all__ = ["settings"]

import os

from dotenv import load_dotenv
from pydantic import BaseConfig
from .db import DBSettings


# ----------------------------------------------------------------
# load env variables
load_dotenv()


# ----------------------------------------------------------------
class Settings(BaseConfig):
    title: str = "ecomseller_task"
    db: DBSettings = DBSettings(
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        name=os.getenv("DB_NAME"),
    )


settings = Settings()
