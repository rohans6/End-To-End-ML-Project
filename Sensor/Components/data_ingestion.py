import pandas as pd
import numpy as np
from Sensor.data_acess.mongo_db_connection import MongoDbClient
from Sensor.Constant.training_pipeline import log_dir
from Sensor.entity.artifact_entity import DataIngestionArtifact
from Sensor.entity.config_entity import DataIngestionConfiguration
import numpy as np
import os
from Sensor.exception import SensorException
from Sensor.logger import Logger
import shutil
from sklearn.model_selection import train_test_split

class DataIngestion:
    def __init__(self,dataingestionconfig):
        #self.log_dir=os.path.join(project_directory,'Logs')
        #if os.path.exists(os.path.join(self.log_dir,'DataIngestion.log')):
            #os.remove(os.path.join(self.log_dir,'DataIngestion.log'))
        self.dataingestionconfig=dataingestionconfig
        self.logger=Logger(log_dir,'DataIngestion.log')  
        self.logger.log_message("Trying to make database object")
        self.database=MongoDbClient()
        self.logger.log_message("Sucessfully created database object")
        self.logger.log_message("Trying to create Artifact and Ingested folders")
        try:
            if os.path.exists(self.dataingestionconfig.dataingestionfolder):
                shutil.rmtree(self.dataingestionconfig.dataingestionfolder)
            os.makedirs(self.dataingestionconfig.dataingestionfolder)
            os.makedirs(self.dataingestionconfig.feature_store)
            os.makedirs(self.dataingestionconfig.ingested_dir)

        except Exception as e:
            raise SensorException("Error occured while creating Artifact and Ingested folders")
        self.logger.log_message("Sucessfully created Artifact and Ingested folders")
    def export_into_feature_store(self):
        self.logger.log_message("Trying to export data into feature store")
        try:
            self.df=self.database.export_as_dataframe()
            print(os.path.exists(os.path.dirname(self.dataingestionconfig.sensor_file)))
            os.makedirs(os.path.dirname(self.dataingestionconfig.sensor_file),exist_ok=True)
            self.df.to_csv(self.dataingestionconfig.sensor_file,index=False,header=True)
        except Exception as e:
            raise SensorException("Error occured while exporting data into feature store")
        self.logger.log_message("Sucessfully exported data into feature store")
        return self.df
    
    def make_train_test_split(self,df):
        self.logger.log_message("Trying to make train and test split")
        try:
            training_df,testing_df=train_test_split(df,test_size=self.dataingestionconfig.testing_split)
            self.logger.log_message("Sucessfully made train and test split")
            os.makedirs(os.path.dirname(self.dataingestionconfig.training_file),exist_ok=True)
            os.makedirs(os.path.dirname(self.dataingestionconfig.testing_file),exist_ok=True)
            training_df.to_csv(self.dataingestionconfig.training_file,index=False,header=True)
            testing_df.to_csv(self.dataingestionconfig.testing_file,index=False,header=True)
            self.logger.log_message("Sucessfully exported training and testing data into Ingested folder")
        except Exception as e:
            raise SensorException("Error occured while making train and test split")
    
    def ingest_data(self):
        df=self.export_into_feature_store()
        self.make_train_test_split(df)
        return DataIngestionArtifact(self.dataingestionconfig.training_file,self.dataingestionconfig.testing_file)
            

