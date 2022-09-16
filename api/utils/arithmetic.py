from cache.redis.decorators import cache


@cache(timeout=60)
def add(a: int, b: int) -> int:
    return a + b
