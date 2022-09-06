from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from database import database
from models import people
from schemas import Person, PersonNoID
from typing import Union, List
import os


app = FastAPI(
    title='FastAPI Tutorial',
    description='This is a FastAPI tutorial.',
    version='1.0.0'
)
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=os.environ.get('CORS_ALLOW_ORIGIN_REGEX'),
    allow_credentials=False,
    allow_methods=['*'],
    allow_headers=['*']
)


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


@app.get('/')
async def root():
    return {'Hello': 'World'}


@app.get('/ip_address', summary='IP Address')
async def ip_address(request: Request):
    ip_address = request.headers.get('X-Forwarded-For', request.client.host)
    port = request.headers.get('X-Forwarded-Port', str(request.client.port))
    return {'ip_address': ip_address, 'port': port}


@app.get('/items/{item_id}')
async def read_item(item_id: int, q: Union[str, None] = None):
    return {'item_id': item_id, 'q': q}


@app.post('/greet')
async def greet(person: PersonNoID):
    greeting = f'Hello {person.name}.'
    age = person.age

    if age is not None and age >= 0:
        greeting += f' You are {age} year old!' if age == 1 else f' You are {age} years old!'
    else:
        greeting += ' How old are you?'

    return {'greeting': greeting}


@app.get('/people', response_model=List[Person])
async def get_people():
    query = people.select()
    return await database.fetch_all(query)


@app.post('/people', response_model=Person, status_code=201)
async def post_data(person: PersonNoID):
    person_dict = person.dict()
    query = people.insert().values(**person_dict)
    _id = await database.execute(query)
    return {**person_dict, 'id': _id}
