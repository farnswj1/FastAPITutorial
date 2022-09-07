from fastapi import APIRouter
from db.database import database
from db.models import people
from schemas.person import Person, PersonNoID
from typing import List


router = APIRouter(prefix='/people', tags=['People'])


@router.post('/greet')
async def greet(person: PersonNoID):
    greeting = f'Hello {person.name}.'
    age = person.age

    if age is not None and age >= 0:
        greeting += f' You are {age} year old!' if age == 1 else f' You are {age} years old!'
    else:
        greeting += ' How old are you?'

    return {'greeting': greeting}


@router.get('', response_model=List[Person])
async def get_people():
    query = people.select()
    return await database.fetch_all(query)


@router.post('', response_model=Person, status_code=201)
async def post_data(person: PersonNoID):
    person_dict = person.dict()
    query = people.insert().values(**person_dict)
    _id = await database.execute(query)
    return {**person_dict, 'id': _id}
