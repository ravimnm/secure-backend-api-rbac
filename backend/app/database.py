from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb+srv://ravi:mongoDB123@cluster0.baksgw3.mongodb.net/restapi_db"

client = AsyncIOMotorClient(MONGO_URL)

db = client["restapi_db"]

users_collection = db["users"]
tasks_collection = db["tasks"]
