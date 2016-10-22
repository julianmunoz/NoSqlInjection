from pymongo import MongoClient

connection = MongoClient()
db = connection['login_database']
collection = db['login_collection']

db.drop_collection("login_collection")

collection.insert_one({'user': 'jmunoz', 'password': 'jmz01', 'email': 'jmz@gmail.com'})
collection.insert_one({'user': 'pepe', 'password': 'pepe01', 'email': 'pepe@gmail.com'})
collection.insert_one({'user': 'jose', 'password': 'josepass', 'email': 'jose90@gmail.com'})