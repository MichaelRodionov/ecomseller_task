import os

from pydantic_settings import BaseSettings


# ----------------------------------------------------------------
class DBSettings(BaseSettings):
    user: str
    password: str
    host: str
    port: str
    name: str

    @property
    def url(self):
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"
