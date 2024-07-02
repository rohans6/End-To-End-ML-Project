from exception import SensorException
from logger import Logger
from Sensor.data_acess import mongo_db_connection
from Sensor.Components.data_ingestion import DataIngestion
from Sensor.Constant.data_ingestion_config import *
from sklearn.model_selection import train_test_split
data_ingestion=DataIngestion()
df=data_ingestion.export_into_feature_store()
data_ingestion.make_train_test_split(df)


