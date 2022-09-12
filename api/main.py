from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware
from db.database import database
from cache.redis import redis
from routes.v1 import router
from config import settings
import logging


logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %z'
)


app = FastAPI(
    title='FastAPI Tutorial',
    description='This is a FastAPI tutorial.',
    version='1.0.0'
)
app.add_middleware(ProxyHeadersMiddleware)
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=settings.ALLOWED_HOSTS
)
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=settings.CORS_ALLOW_ORIGIN_REGEX,
    allow_credentials=False,
    allow_methods=['*'],
    allow_headers=['*']
)
app.include_router(router)


@app.on_event('startup')
async def startup():
    await database.connect()
    await redis.ping()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()
    await redis.close()
