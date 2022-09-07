from sqlalchemy import MetaData, Table, Column, Integer, String, create_engine
from config import settings


metadata = MetaData()

people = Table(
    'people',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(30), nullable=False),
    Column('age', Integer, nullable=False)
)

engine = create_engine(settings.DATABASE_URL)
metadata.create_all(engine)
