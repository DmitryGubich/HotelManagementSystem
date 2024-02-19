from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Setting(BaseSettings):
    MODE: Literal["DEV", "TEST", "PROD"]
    DATABASE_URL: str
    POSTGRES_PASSWORD: str
    SECRET_KEY: str
    ALGORITHM: str
    SENTRY_DSN: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Setting()
