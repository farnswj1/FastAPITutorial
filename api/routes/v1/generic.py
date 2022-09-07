from fastapi import APIRouter, Request
from cache.redis import redis
from typing import Union


router = APIRouter(tags=['Generic'])


@router.get('/')
async def root():
    return {'Hello': 'World'}


@router.get('/ip_address', summary='IP Address')
async def ip_address(request: Request):
    ip_address = request.headers.get('X-Forwarded-For', request.client.host)
    port = request.headers.get('X-Forwarded-Port', str(request.client.port))
    return {'ip_address': ip_address, 'port': port}


@router.get('/items/{item_id}')
async def read_item(item_id: int, q: Union[str, None] = None):
    return {'item_id': item_id, 'q': q}


@router.get('/add')
async def add(a: int, b: int):
    min_val, max_val = (b, a) if a > b else (a, b)
    cache_key = f'add_{min_val}_{max_val}'
    result = await redis.get(cache_key)

    if result is None:
        result = a + b
        await redis.set(cache_key, result, ex=60)
    else:
        result = int(result)

    return result
