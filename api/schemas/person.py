from pydantic import BaseModel


class PersonNoID(BaseModel):
    name: str
    age: int


class Person(BaseModel):
    id: int
    name: str
    age: int
