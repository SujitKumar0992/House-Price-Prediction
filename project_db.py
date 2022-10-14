import pickle

from pymongo import MongoClient
import config
from dotenv import load_dotenv
import os

database = config.DATABASE



load_dotenv()  # use dotenv to hide sensitive credential as environment variables
DATABASE_URL = f'mongodb+srv://JR-Test:{os.environ.get("password")}'/'@cluster0.5uasnpw.mongodb.net/database?'/'retryWrites=true&w=majority'

mongo_db_client = MongoClient(DATABASE_URL)

db = mongo_db_client[database]

collection_user = db['user_details']


def register_user(data):
    print('******************************************************')
    name = data["name"]
    email = data['email']
    password = data['password']

    collection_user.insert_one({'name': name, 'email': email, 'password': password})

    response = collection_user.find_one({'email': email, 'password': password})

    return response


def login_user(data):
    print("********************************************************************")
    email = data['email']
    password = data['password']

    response = collection_user.find_one({'email': email, 'password': password})

    return response
