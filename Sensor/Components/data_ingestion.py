import pandas as pd
import numpy as np
from Sensor.data_acess.mongo_db_connection import MongoDbClient
from Sensor.Constant.data_ingestion_config import *
import numpy as np
import os
from exception import SensorException
from logger import Logger
import shutil
from sklearn.model_selection import train_test_split
class DataIngestion:
    def __init__(self):
        self.log_dir=os.path.join(project_directory,'Logs')
        if os.path.exists(os.path.join(self.log_dir,'DataIngestion.log')):
            os.remove(os.path.join(self.log_dir,'DataIngestion.log'))
        self.logger=Logger(self.log_dir,'DataIngestion.log')  
        self.logger.log_message("Trying to make database object")
        self.database=MongoDbClient()
        self.logger.log_message("Sucessfully created database object")
        self.logger.log_message("Trying to create Artifact and Ingested folders")
        try:
            if not os.path.exists(artifact_directory):
                os.makedirs(artifact_directory)
                os.makedirs(feature_store)
                os.makedirs(ingested)
            else: 
                shutil.rmtree(artifact_directory)
                os.makedirs(artifact_directory)
                os.makedirs(feature_store)
                os.makedirs(ingested)

        except Exception as e:
            print(SensorException("Error occured while creating Artifact and Ingested folders"))
        self.logger.log_message("Sucessfully created Artifact and Ingested folders")
    def export_into_feature_store(self):
        self.logger.log_message("Trying to export data into feature store")
        try:
            self.df=self.database.export_as_dataframe()
            self.df.to_csv(sensor_file)
        except Exception as e:
            print(SensorException("Error occured while exporting data into feature store"))
        self.logger.log_message("Sucessfully exported data into feature store")
        return self.df
    
    def make_train_test_split(self,df):
        self.logger.log_message("Trying to make train and test split")
        try:
            training_df,testing_df=train_test_split(df,test_size=testing_split)
            self.logger.log_message("Sucessfully made train and test split")
            print("Training data shape",training_df.shape)
            print("Testing data shape",testing_df.shape)
            training_df.to_csv(training_file)
            testing_df.to_csv(testing_file)
            self.logger.log_message("Sucessfully exported training and testing data into Ingested folder")
        except Exception as e:
            print(SensorException("Error occured while making train and test split"))
            

