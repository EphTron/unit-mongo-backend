import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import pymongo
from pymongo import MongoClient

config_str = ""
with open('config.txt', 'r') as f:
    config_str = f.read()
    print(config_str)

#conn = pymongo.Connection(config_str)
client = pymongo.MongoClient(config_str)

db = client['users']

print(db.list_collections())

