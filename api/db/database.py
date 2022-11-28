from databases import Database
from sqlalchemy import MetaData
from config import settings


database = Database(settings.DATABASE_URL)

metadata = MetaData()
