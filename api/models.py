from sqlalchemy import MetaData, Table, Column, Integer, String, create_engine
import os


metadata = MetaData()

people = Table(
    'people',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(30), nullable=False),
    Column('age', Integer, nullable=False)
)

engine = create_engine(os.environ.get('DATABASE_URL'))
metadata.create_all(engine)
