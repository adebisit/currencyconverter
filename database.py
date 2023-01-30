from pymongo import MongoClient
from config import settings


client = MongoClient(settings.ATLAS_URI)
print('Connected to MongoDB...')
db = client[settings.DB_NAME]