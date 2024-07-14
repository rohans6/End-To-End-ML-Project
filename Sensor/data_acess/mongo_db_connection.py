import pymongo
from Sensor.exception import SensorException
from Sensor.logger import Logger
from Sensor.Constant.database import *
import numpy as np
import pandas as pd


class MongoDbClient:
    def __init__(self):
        try:
            self.mongodbclient=pymongo.MongoClient(url)
            self.db=self.mongodbclient[database]
            if not collection_name in self.db.list_collection_names():
                print(f"{collection_name} does not exist!")
            self.collection=self.db[collection_name]
        except Exception:
            raise SensorException("MongoDb Connection Error")
    def export_as_dataframe(self):
        try:
            data=list(self.collection.find())
            self.df=pd.DataFrame(data)
            self.df.drop(columns=['_id'],axis=1,inplace=True)
            self.df=self.df.replace({'na':np.nan})
            return self.df
        except Exception:
            raise SensorException("Error occured whil exporting mongo db data to dataframe")

        

