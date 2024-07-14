from Sensor.exception import SensorException
import os
from Sensor.Constant.training_pipeline import model_name
class SensorModel:
    def __init__(self,preprocessor,model):
        self.model=model
        self.preprocessor=preprocessor
    def predict(self,X):
        try:
            X_preprocessed=self.preprocessor.transform(X)
            return self.model.predict(X_preprocessed)
        except Exception as e:
            raise SensorException("Error occurred while making predictions")

class ModelResolver:
    def __init__(self,saved_model_dir):
        self.saved_model_dir=saved_model_dir
    def get_latest_model_path(self):
        try:
            timestamps=os.listdir(self.saved_model_dir)
            latest_timestamp=max([int(timestamp) for timestamp in timestamps])
            latest_model_path=os.path.join(self.saved_model_dir,str(latest_timestamp),model_name)
            return latest_model_path
        except Exception as e:
            raise SensorException("Error occurred while getting the latest model path")
    def is_model_exists(self):
        try:
            if not os.path.exists(self.saved_model_dir):
                return False
            timestamps=os.listdir(self.saved_model_dir)
            if len(timestamps) == 0:
                return False
            latest_model_path=self.get_latest_model_path()
            if not os.path.exists(latest_model_path):
                return False
            return True
        except Exception as e:
            raise SensorException("Error occurred while checking model existence")
            
    