import sys,os,shutil
from Sensor.entity.config_entity import ModelPusherConfiguration
from Sensor.entity.artifact_entity import ModelPusherArtifact
from Sensor.logger import Logger
from Sensor.exception import SensorException
from Sensor.Constant.training_pipeline import log_dir

class ModelPusher:
    def __init__(self,modelevaluationartifact,modelpusherconfiguration):
        self.modelevaluationartifact = modelevaluationartifact
        self.modelpusherconfiguration = modelpusherconfiguration
        self.logger = Logger(log_dir, 'ModelPusher.log')
    def push_model(self):
        try:
            model_file_path=self.modelevaluationartifact.trained_model_path
            destination=self.modelpusherconfiguration.model_pusher_file_path
            os.makedirs(os.path.dirname(destination),exist_ok=True)
            shutil.copy(src=model_file_path, dst=destination)

            destination=self.modelpusherconfiguration.saved_model_file_path
            os.makedirs(os.path.dirname(destination),exist_ok=True)
            shutil.copy(src=model_file_path, dst=destination)

            return ModelPusherArtifact(self.modelpusherconfiguration.model_pusher_file_path,self.modelpusherconfiguration.saved_model_file_path)

            

        except Exception as e:
            raise SensorException("Error occurred while pushing model")