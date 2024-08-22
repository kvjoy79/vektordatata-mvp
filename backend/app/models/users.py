from pymongo import MongoClient
"""
This module contains the User model for the Vektor-Data application.
Attributes:
    client (pymongo.MongoClient): The MongoDB client object.
    db (pymongo.database.Database): The MongoDB database object.
    users (pymongo.collection.Collection): The collection object for the 'users' collection in the database.
"""
from dotenv import load_dotenv
import os

load_dotenv()
client = MongoClient(os.getenv('MONGO_URI'))
db = client['Vektor-Data']

users = db.users
