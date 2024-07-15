from pymongo import MongoClient
import certifi
from app.core.config import settings

ca = certifi.where()

client = MongoClient(settings.MONGODB_URI, tls=True, tlsCAFile=ca)

db = client.wof_db

user_collection = db["user_collection"]
image_collection = db["image_collection"]

user_collection.create_index('username', unique=True)