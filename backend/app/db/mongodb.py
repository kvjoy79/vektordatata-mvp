from dotenv import load_dotenv
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()


def get_mongodb_client():
    """
    Retrieves the MongoDB database connection.

    Returns:
        MongoClient: A client connected to the MongoDB database.
    """
    mongo_uri = os.getenv('MONGO_URI')
    client = MongoClient(mongo_uri, server_api=ServerApi('1'))
    print(client.list_database_names())
    return client

def connect_to_db():
    """
    Connects to the MongoDB database and confirms the connection.
    """
    client =  get_mongodb_client()

    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")



