from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Union

app = FastAPI(
    title='FastAPI Tutorial',
    description='This is a FastAPI tutorial.',
    version='1.0.0'
)


class Person(BaseModel):
    name: str
    age: Union[int, None] = None


@app.get('/')
def root():
    return {'Hello': 'World'}


@app.get('/ip_address', summary='IP Address')
def ip_address(request: Request):
    ip_address = request.headers.get('X-Forwarded-For', request.client.host)
    port = request.headers.get('X-Forwarded-Port', str(request.client.port))
    return {'ip_address': ip_address, 'port': port}


@app.get('/items/{item_id}')
def read_item(item_id: int, q: Union[str, None] = None):
    return {'item_id': item_id, 'q': q}


@app.post('/greet')
def greet(person: Person):
    greeting = f'Hello {person.name}.'
    age = person.age

    if age is not None and age >= 0:
        greeting += f' You are {age} year old!' if age == 1 else f' You are {age} years old!'
    else:
        greeting += ' How old are you?'

    return {'greeting': greeting}
