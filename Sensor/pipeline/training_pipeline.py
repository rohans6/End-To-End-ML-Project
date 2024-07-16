from Sensor.Components.data_ingestion import DataIngestion
from Sensor.Components.data_validation import DataValidation
from Sensor.Components.data_transformation import DataTransformer
from Sensor.Components.model_trainer import ModelTrainer
from Sensor.Components.model_evaluation import ModelEvaluation
from Sensor.Components.model_pusher import ModelPusher
from Sensor.entity.config_entity import DataIngestionConfiguration,DataValidationConfiguration,DataTransformerConfiguration,ModelTrainerConfiguration,ModelPusherConfiguration,ModelEvaluatorConfiguration
from Sensor.logger import Logger
from Sensor.exception import SensorException
from Sensor.Constant.training_pipeline import log_dir
import os
class TrainingPipeline:
    def __init__(self):
        self.dataingestionconfig=DataIngestionConfiguration()
        self.logger=Logger(log_dir, "training_pipeline.log")
    def start_ingestion(self):
        try:
            self.ingester=DataIngestion(self.dataingestionconfig)
            dataingestionart=self.ingester.ingest_data()
            return dataingestionart

        except Exception as e:
            raise SensorException("Error occurred while ingesting data")
    def start_validation(self,dataingestionart):
        try:
            self.validator=DataValidation(dataingestionart,DataValidationConfiguration())
            datavalidationart=self.validator.validate_data()
            return datavalidationart
        except Exception as e:
            raise SensorException("Error occurred while validating data")
    def start_transformation(self,datavalidationart):
        try:
            self.transformer=DataTransformer(datavalidationart,DataTransformerConfiguration())
            datatransformerart=self.transformer.transform_data()
            return datatransformerart
        except Exception as e:
            raise SensorException("Error occurred while transforming data")
    def start_model_trainer(self,datatransformerart):
        try:
            self.trainer=ModelTrainer(datatransformerart,ModelTrainerConfiguration())
            modeltrainerart=self.trainer.train_model()
            return modeltrainerart
        except Exception as e:
            raise SensorException("Error occurred while training the model")
    def start_model_evaluator(self,datavalidationart,modeltrainerart):
        try:
            self.evaluator=ModelEvaluation(datavalidationart,modeltrainerart,ModelEvaluatorConfiguration())
            evaluationart=self.evaluator.evaluate_model()
            return evaluationart
        except Exception as e:
            raise SensorException("Error occurred while evaluating the model")
    def start_pusher(self,evaluationart):
        try:
            self.pusher=ModelPusher(evaluationart,ModelPusherConfiguration())
            pusherart=self.pusher.push_model()
            return pusherart
        except Exception as e:
            raise SensorException("Error occurred while pushing the model")
    def start_pipeline(self):
        try:
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
            return pusherart
        except Exception as e:
            raise SensorException("Error occurred while running the training pipeline")

