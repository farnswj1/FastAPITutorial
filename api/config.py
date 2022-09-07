from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    DATABASE_URL: str = os.environ.get('DATABASE_URL')
    REDIS_URL: str = os.environ.get('REDIS_URL')
    CORS_ALLOW_ORIGIN_REGEX: str = os.environ.get('CORS_ALLOW_ORIGIN_REGEX')


settings = Settings()
