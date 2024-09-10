from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os

# Load your MongoDB credentials from environment variables for security
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb+srv://<db_username>:<db_password>@floristadb.et9vl.mongodb.net/?retryWrites=true&w=majority&appName=floristadb")

def connect_db():
    # Create a new client and connect to the server
    client = MongoClient(MONGODB_URI, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        db = client['florist_db']
        return db
    except Exception as e:
        print("Failed to connect to MongoDB", e)
        raise

db = connect_db()
