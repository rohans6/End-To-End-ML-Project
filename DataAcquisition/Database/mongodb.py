from pymongo import MongoClient
from . import mongodb_credensials
class MongoDb:
    def __init__(self):
        self.connection=MongoClient(mongodb_credensials["url"])
        self.db=self.connection[mongodb_credensials['database']]
    def create(self,collection_name='sensor'):
        self.collection=collection_name
        self.db.create_collection(collection_name)
    def insert_one(self,document):
        self.db[self.collection].insert_one(document)
    def insert_many(self,documents):
        self.db[self.collection].insert_many(documents)
    def close(self):pass