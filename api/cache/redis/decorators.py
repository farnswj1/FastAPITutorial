from cache.redis import redis
from urllib.parse import quote
from typing import Any, Awaitable, Callable
import asyncio


def cache(timeout: int | None = None) -> Callable:
    def decorator_func(func: Callable | Awaitable) -> Awaitable[Any]:
        is_async_function = asyncio.iscoroutinefunction(func)
        module = func.__module__
        name = func.__name__
        func_path = f'{module}.{name}' if module else name

        # Delete the references since they're no longer needed
        del module
        del name

        def _get_cache_key(*args, **kwargs) -> str:
            cache_key = func_path

            if args:
                args_str = quote('_'.join(map(str, args)))
                cache_key += f'__{args_str}'

            if kwargs:
                kwargs_str = quote(
                    '_'.join(f'{key}={value}' for key, value in sorted(kwargs.items()))
                )
                cache_key += f'__{kwargs_str}'

            return cache_key

        async def wrapper(*args, **kwargs) -> Any:
            cache_key = _get_cache_key(*args, **kwargs)
            result = await redis.get(cache_key)

            if result is None:
                if is_async_function:
                    result = await func(*args, **kwargs)
                else:
                    result = func(*args, **kwargs)

                await redis.set(cache_key, result, timeout)

            return result
        return wrapper
    return decorator_func
