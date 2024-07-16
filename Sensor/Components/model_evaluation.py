
from Sensor.Constant.training_pipeline import log_dir,project_directory,saved_model_dir,model_name,schema_file
from Sensor.utils.main_utils import read_yaml_file
from Sensor.logger import Logger
from Sensor.exception import SensorException
from Sensor.ml.model.estimator import ModelResolver
from Sensor.entity.artifact_entity import ModelEvaluatorArtifact
import os
import pandas as pd
from Sensor.utils.main_utils import load_object
import sklearn.metrics as metrics
class ModelEvaluation:
    def __init__(self,datavalidationartifact,modeltrainerartifact,modelevaluationconfig):
        try:
            self.datavalidationartifact=datavalidationartifact
            self.modeltrainerartifact=modeltrainerartifact
            self.modelevaluationconfig=modelevaluationconfig
            self.logger=Logger(log_dir,'ModelEvaluation.log')
            self.schema_file=read_yaml_file(schema_file)
            self.drop_cols=self.schema_file.get('drop_columns')
        except Exception as e:
            raise SensorException("Error occurred while reading modelevaluation config")
    def evaluate_model(self):
        path=os.path.join(project_directory,saved_model_dir)
        try:
            model_resolver=ModelResolver(path)
            if not model_resolver.is_model_exists():
                self.logger.log_message("No trained model found in the specified directory")
                return ModelEvaluatorArtifact(True,None,self.modeltrainerartifact.trained_model_path)
            self.logger.log_message("Models found in saved models directory")
            test_df=pd.read_csv(self.datavalidationartifact.valid_test_path)
            test_df=test_df.drop(self.drop_cols,axis=1)
            features,labels=test_df.drop('class',axis=1),test_df['class']
            labels=labels.replace({'pos':1,'neg':0})
            trained_model=load_object(self.modeltrainerartifact.trained_model_path)
            trained_predictions=trained_model.predict(features)
            trained_f1=metrics.f1_score(labels,trained_predictions)
            best_model=self.modeltrainerartifact.trained_model_path
            is_model_accepted=True
            self.logger.log_message("Performed prediction on test dataset using recent model and obtained f1 score")
            latest_model_path=model_resolver.get_latest_model_path()
            latest_model=load_object(latest_model_path)
            latest_predictions=latest_model.predict(features)
            latest_f1=metrics.f1_score(labels,latest_predictions)
            print(trained_f1,latest_f1)
            if trained_f1-latest_f1<=self.modelevaluationconfig.threshold:
                is_model_accepted=False
            #for timestamp in os.listdir(path):
                #previous_model=load_object(os.path.join(path,timestamp,model_name))
                #previous_predictions=previous_model.predict(features)
                #previous_f1=metrics.f1_score(labels,previous_predictions)
                #if previous_f1>trained_f1:
                    #best_model=os.path.join(path,timestamp,model_name)
                    #is_model_accepted=False
            self.logger.log_message("Done with comparing with all previous models")
            return ModelEvaluatorArtifact(is_model_accepted,best_model,self.modeltrainerartifact.trained_model_path)
        except Exception as e:
            raise SensorException("Error occurred while evaluating model")




