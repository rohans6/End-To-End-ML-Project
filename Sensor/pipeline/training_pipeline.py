from Sensor.Components.data_ingestion import DataIngestion
from Sensor.Components.data_validation import DataValidation
from Sensor.Components.data_transformation import DataTransformer
from Sensor.Components.model_trainer import ModelTrainer
from Sensor.Components.model_evaluation import ModelEvaluation
from Sensor.Components.model_pusher import ModelPusher
from Sensor.entity.config_entity import DataIngestionConfiguration,DataValidationConfiguration,DataTransformerConfiguration,ModelTrainerConfiguration,ModelPusherConfiguration,ModelEvaluatorConfiguration,TrainingPipelineConfig
from Sensor.logger import Logger
from Sensor.exception import SensorException
from Sensor.Constant.training_pipeline import log_dir
from Sensor.Constant.s3_bucket import training_bucket,prediction_bucket
import os
from Sensor.cloud_storage.s3_syncer import S3Sync
from Sensor.Constant.training_pipeline import saved_model_dir
import sys
class TrainingPipeline:
    def __init__(self):
        #self.dataingestionconfig=DataIngestionConfiguration()
        self.logger=Logger(log_dir, "training_pipeline.log")
        self.training_pipeline_config=TrainingPipelineConfig()
        self.dataingestionconfig=DataIngestionConfiguration(self.training_pipeline_config)
        self.is_running=False
        self.s3syncer = S3Sync()
    def start_ingestion(self):
        try:
            self.ingester=DataIngestion(self.dataingestionconfig)
            dataingestionart=self.ingester.ingest_data()
            return dataingestionart

        except Exception as e:
            raise SensorException("Error occurred while ingesting data")
    def start_validation(self,dataingestionart):
        try:
            self.validator=DataValidation(dataingestionart,DataValidationConfiguration(self.training_pipeline_config))
            datavalidationart=self.validator.validate_data()
            return datavalidationart
        except Exception as e:
            raise SensorException("Error occurred while validating data")
    def start_transformation(self,datavalidationart):
        try:
            self.transformer=DataTransformer(datavalidationart,DataTransformerConfiguration(self.training_pipeline_config))
            datatransformerart=self.transformer.transform_data()
            return datatransformerart
        except Exception as e:
            raise SensorException("Error occurred while transforming data")
    def start_model_trainer(self,datatransformerart):
        try:
            self.trainer=ModelTrainer(datatransformerart,ModelTrainerConfiguration(self.training_pipeline_config))
            modeltrainerart=self.trainer.train_model()
            return modeltrainerart
        except Exception as e:
            raise SensorException("Error occurred while training the model")
    def start_model_evaluator(self,datavalidationart,modeltrainerart):
        try:
            self.evaluator=ModelEvaluation(datavalidationart,modeltrainerart,ModelEvaluatorConfiguration(self.training_pipeline_config))
            evaluationart=self.evaluator.evaluate_model()
            return evaluationart
        except Exception as e:
            raise SensorException("Error occurred while evaluating the model")
    def start_pusher(self,evaluationart):
        try:
            self.pusher=ModelPusher(evaluationart,ModelPusherConfiguration(self.training_pipeline_config))
            pusherart=self.pusher.push_model()
            return pusherart
        except Exception as e:
            raise SensorException("Error occurred while pushing the model")
    def sync_artifact_dir_to_s3(self):
        try:
            aws_buket_url = f"s3://{training_bucket}/artifact/{self.training_pipeline_config.timestamp}"
            self.s3syncer.sync_folder_to_s3(folder = self.training_pipeline_config.artifact_dir,aws_buket_url=aws_buket_url)
        except Exception as e:
            raise SensorException(e,sys)
            
    def sync_saved_model_dir_to_s3(self):
        try:
            saved_models=os.path.join("saved_models")
            aws_buket_url = f"s3://{training_bucket}/{saved_model_dir}"
            self.s3syncer.sync_folder_to_s3(folder = saved_model_dir,aws_buket_url=aws_buket_url)
        except Exception as e:
            raise SensorException(e,sys)
    def start_pipeline(self):
        try:
            self.is_running = True
            dataingestionart=self.start_ingestion()
            self.logger.log_message("Data ingestion completed successfully")
            datavalidationart=self.start_validation(dataingestionart)
            self.logger.log_message("Data validation completed successfully")
            datatransformerart=self.start_transformation(datavalidationart)
            self.logger.log_message("Data transformation completed successfully")
            modeltrainerart=self.start_model_trainer(datatransformerart)
            self.logger.log_message("Model training completed successfully")
            evaluationart=self.start_model_evaluator(datavalidationart,modeltrainerart)
            print(evaluationart)
            self.logger.log_message("Model evaluation completed successfully")
            if not evaluationart.is_model_accepted:
                raise SensorException("Model evaluation result is not accepted")
            pusherart=self.start_pusher(evaluationart)
            self.logger.log_message("Model pushing completed successfully")
            self.is_running = False
            self.sync_artifact_dir_to_s3()
            self.sync_saved_model_dir_to_s3()
            return pusherart
        except Exception as e:
            self.sync_artifact_dir_to_s3()
            raise SensorException("Error occurred while running the training pipeline")

