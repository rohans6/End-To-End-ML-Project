from pymongo import MongoClient
from . import mongodb_credensials
class MongoDb:
    def __init__(self):
        self.connection=MongoClient(mongodb_credensials["url"])
        self.db=self.connection.mongodb_credensials['database']
    def create(self):
        self.db.create_collection('sensor')
    def insert_one(self,document):
        self.collection.insert_one(document)
    def insert_many(self,documents):
        self.collection.insert_many(documents)
    def close(self):pass