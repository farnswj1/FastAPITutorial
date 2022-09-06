from databases import Database
import os


database = Database(os.environ.get('DATABASE_URL'))
