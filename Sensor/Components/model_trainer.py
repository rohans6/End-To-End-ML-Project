from Sensor.utils.main_utils import load_numpy_array,load_object,save_object
from Sensor.entity.artifact_entity import ModelTrainerArtifact
from Sensor.entity.config_entity import ModelTrainerConfiguration
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
from Sensor.Constant.training_pipeline import log_dir
from Sensor.logger import Logger
from Sensor.exception import SensorException
from Sensor.ml.metric.classification_report import get_classification_report
import os
import shutil
from Sensor.ml.model.estimator import SensorModel
import shutil
class ModelTrainer:
    def __init__(self,datatransformationartifact,modeltrainingconfig):
        self.datatransformationartifact = datatransformationartifact
        self.modeltrainingconfig = modeltrainingconfig
        self.model=LogisticRegression(solver='lbfgs')
        self.logger=Logger(log_dir,'ModelTrainer.log')
        if os.path.exists(self.modeltrainingconfig.modeltrainingfolder):
            shutil.rmtree(self.modeltrainingconfig.modeltrainingfolder)
        os.makedirs(self.modeltrainingconfig.modeltrainingfolder)
    def train_model(self):
        train,test=load_numpy_array(self.datatransformationartifact.transformed_train_path),load_numpy_array(self.datatransformationartifact.transformed_test_path)
        X_train,y_train=train[:,:-1],train[:,-1]
        X_test,y_test=test[:,:-1],test[:,-1]
        self.logger.log_message("Sucessfully partitioned data into features and labels")
        self.model.fit(X_train,y_train)
        self.logger.log_message("Sucessfully trained model")
        train_predictions=self.model.predict(X_train)
        test_predictions=self.model.predict(X_test)
        self.logger.log_message("Sucessfully generated predictions")
        report=get_classification_report(y_train,train_predictions,y_test,test_predictions)
        self.logger.log_message("Sucessfully generated classification report")
        #if os.path.exists(self.modeltrainingconfig.trained_model_filepath):
            #os.remove(self.modeltrainingconfig.trained_model_filepath)
        #directory=os.path.dirname(self.modeltrainingconfig.trained_model_filepath)
        #os.makedirs(directory,exist_ok=True)
        preprocessor_obj=load_object(self.datatransformationartifact.preprocessing_obj)
        sensor_model=SensorModel(preprocessor_obj,self.model)

        save_object(self.modeltrainingconfig.trained_model_filepath,sensor_model)
        self.logger.log_message("Sucessfully saved trained model")
        return ModelTrainerArtifact(self.modeltrainingconfig.trained_model_filepath,report)











