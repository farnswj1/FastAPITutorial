from redis.asyncio import Redis
from redis.commands.core import ResponseT
from config import settings
from typing import Any
import pickle


class RedisCache(Redis):
    @staticmethod
    def serialize(value: Any = None) -> int | bytes:
        return value if type(value) is int else pickle.dumps(value, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def deserialize(value: str | bytes | None = None) -> Any:
        if value is None:
            return value

        try:
            return int(value)
        except ValueError:
            return pickle.loads(value)

    async def set(self, name: str | bytes, value: Any, *args, **kwargs) -> ResponseT:
        _value = self.serialize(value)
        return await super().set(name, _value, *args, **kwargs)

    async def get(self, name: str | bytes) -> Any:
        value = await super().get(name)
        return self.deserialize(value)


redis = RedisCache.from_url(settings.REDIS_URL)
