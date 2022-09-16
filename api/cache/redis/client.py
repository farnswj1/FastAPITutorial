from redis.asyncio import Redis
from redis.commands.core import ResponseT
from config import settings
from typing import Any, TypeAlias
import pickle


_Key: TypeAlias = str | bytes


class RedisCache(Redis):
    @staticmethod
    def serialize(value: Any = None) -> int | bytes:
        return value if type(value) is int else pickle.dumps(value, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def deserialize(value: _Key | None = None) -> Any:
        try:
            return int(value)
        except ValueError:
            return pickle.loads(value)

    async def set(self, name: _Key, value: Any, *args, **kwargs) -> ResponseT:
        _value = self.serialize(value)
        return await super().set(name, _value, *args, **kwargs)

    async def get(self, name: _Key, default: Any = None) -> Any:
        value = await super().get(name)
        return default if value is None else self.deserialize(value)


redis = RedisCache.from_url(settings.REDIS_URL)
