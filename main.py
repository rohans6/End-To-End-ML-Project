from Sensor.exception import SensorException
from Sensor.logger import Logger
from Sensor.data_acess import mongo_db_connection
from Sensor.Components.data_ingestion import DataIngestion
from Sensor.Constant.data_ingestion_config import *
from Sensor.Components.data_validation import DataValidation
from Sensor.Components.data_transformation import DataTransformer
from Sensor.Components.model_trainer import ModelTrainer
from Sensor.Components.model_evaluation import ModelEvaluation
from Sensor.Components.model_pusher import ModelPusher
from Sensor.entity.artifact_entity import DataIngestionArtifact,DataTransformerArtifact,ModelTrainerArtifact
from Sensor.entity.config_entity import DataValidationConfiguration,DataTransformerConfiguration,ModelTrainerConfiguration,ModelPusherConfiguration
from sklearn.model_selection import train_test_split
import pandas as pd
import shutil
from Sensor.utils.main_utils import read_yaml_file
from Sensor.Constant.training_pipeline import schema_file
#shutil.rmtree(artifact_directory)
#data_ingestion=DataIngestion()

#df=data_ingestion.export_into_feature_store()
#data_ingestion.make_train_test_split(df)

#train_path,test_path='D:\\DataScience\\Projects\\SensorProject\\End-To-End-ML-Project\\Artifact\\ingested\\training_data.csv','D:\\DataScience\\Projects\\SensorProject\\End-To-End-ML-Project\\Artifact\\ingested\\testing_data.csv'
#train_path=train_path.replace('\\','/')
#test_path=test_path.replace('\\','/')
#ingestion_art=DataIngestionArtifact(train_path,test_path)
#validation_config=DataValidationConfiguration()
#data_valid=DataValidation(ingestion_art,validation_config)
#valid_config=data_valid.validate_data()
#print(valid_config)
#transform_confg=DataTransformationConfiguration()

#transformer=DataTransformation(valid_config,transform_confg)
#transform_art=transformer.transform_data()
#print(transform_art)

#data_transformation_artifact=DataTransformationArtifact(transform_art)
#model_trainer_config=ModelTrainerConfiguration()

#trainer=ModelTrainer(transform_art,model_trainer_config)
#model_trainer_config=trainer.train_model()

#evaluator=ModelEvaluation(valid_config,model_trainer_config,None)
#evaluation_config=evaluator.evaluate_model()
#print(evaluation_config)
from Sensor.pipeline.training_pipeline import TrainingPipeline
from Sensor.entity.config_entity import DataIngestionConfiguration,DataValidationConfiguration,DataTransformerConfiguration,ModelTrainerConfiguration,ModelPusherConfiguration,ModelEvaluatorConfiguration,TrainingPipelineConfig
training_config=TrainingPipelineConfig()
#data_ingestion_config=DataIngestionConfiguration(training_config)
#data_ingester=DataIngestion(data_ingestion_config)
#art=data_ingester.ingest_data()
tr=TrainingPipeline()
pusher_art=tr.start_pipeline()