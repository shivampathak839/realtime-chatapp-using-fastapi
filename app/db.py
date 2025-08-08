import motor.motor_asyncio

MONGO_DETAILS = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.chat_db
chat_collection = database.get_collection("chats")
users_collection = database.get_collection("users")