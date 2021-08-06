import pymongo
from pymongo import MongoClient

client = MongoClient()

client = MongoClient('localhost', 27017)

db = client.test_database
collection = db.test_collection

posts = db.posts

my_post = {"name":"Ephra",
           "age":31}

post_id = posts.insert_one(my_post).inserted_id
print(post_id)