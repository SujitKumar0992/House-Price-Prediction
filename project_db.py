import pickle

from pymongo import MongoClient
import config

database=config.DATABASE

mongodb_port=27017

uri=f'mongodb://localhost:{mongodb_port}/'

mongo_db_client= MongoClient(uri)

db=mongo_db_client[database]

collection_user = db['user_details']


def register_user(data):
    print('******************************************************')
    name= data["name"]
    email = data['email']
    password = data['password']

    collection_user.insert_one({'name': name, 'email': email, 'password': password})

    response=collection_user.find_one({'email':email,'password':password})

    return response




def login_user(data):
    print("********************************************************************")
    email = data['email']
    password=data['password']

    response = collection_user.find_one({'email': email, 'password': password})

    return response








