from pymongo import MongoClient



MONGO_URL = "mongodb+srv://test123:12345@cluster0.njmfbiw.mongodb.net/"
conn = MongoClient(MONGO_URL)

db = conn.realestate

user_collection = db["user"]
realestate_collection = db["realestate"]

