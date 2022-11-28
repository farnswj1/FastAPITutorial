from sqlalchemy import Table, Column, Integer, String, Boolean
from db.database import metadata


people = Table(
    'people',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(30), nullable=False),
    Column('age', Integer, nullable=False)
)
