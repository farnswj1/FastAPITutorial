from fastapi import APIRouter, Request
from utils.arithmetic import add


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
async def read_item(item_id: int, q: str | None = None):
    return {'item_id': item_id, 'q': q}


@router.get('/add')
async def add_numbers(a: int, b: int):
    min_val, max_val = (b, a) if a > b else (a, b)
    return await add(min_val, max_val)
