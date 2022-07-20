from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()


class Person(BaseModel):
    name: str
    age: Union[int, None] = None


@app.get('/')
def root():
    return {'Hello': 'World'}


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
