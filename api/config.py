from pydantic import BaseSettings
from typing import Any, List


class Settings(BaseSettings):
    ALLOWED_HOSTS: List[str]
    CORS_ALLOW_ORIGIN_REGEX: str
    DATABASE_URL: str
    REDIS_URL: str

    class Config(BaseSettings.Config):
        @classmethod
        def parse_env_var(cls, field_name: str, raw_val: str) -> Any:
            if field_name == 'ALLOWED_HOSTS':
                return raw_val.split()
            return cls.json_loads(raw_val)


settings = Settings()
