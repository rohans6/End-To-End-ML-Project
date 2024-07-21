from Sensor.entity.artifact_entity import DataTransformerArtifact
from Sensor.entity.config_entity import DataTransformerConfiguration
from Sensor.exception import SensorException
from Sensor.logger import Logger
from Sensor.Constant.training_pipeline import log_dir,target_col,knearest_neighbors,resampling_strategy
from sklearn.impute import KNNImputer
from sklearn.preprocessing import StandardScaler,RobustScaler,PowerTransformer
from sklearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE
import pandas as pd
import numpy as np
from Sensor.utils.main_utils import save_numpy_array,save_object,read_yaml_file
from Sensor.Constant.training_pipeline import schema_file
import os
import shutil
class DataTransformer:
    def __init__(self,datavalidtionartifact,datatransformationconfig):
        self.datavalidationartifact=datavalidtionartifact
        self.datatransformationconfig=datatransformationconfig
        self.logger=Logger(log_dir,'DataTransformer.log')
        if not self.datavalidationartifact.validation_status:
            raise SensorException("Data validation failed. Please check the data validation artifact.")
        if os.path.exists(self.datatransformationconfig.datatransformationfolder):
                shutil.rmtree(self.datatransformationconfig.datatransformationfolder)
        os.makedirs(self.datatransformationconfig.datatransformationfolder)
        self.preprocessor_obj=Pipeline([('PowerTransformer',PowerTransformer(method='yeo-johnson')),('Scaler',RobustScaler()),('KNN imputer',KNNImputer(n_neighbors=knearest_neighbors))])
        self.smt=SMOTE(sampling_strategy=resampling_strategy)
        self.drop_columns=read_yaml_file(schema_file)['drop_columns']
    @staticmethod
    def read_data(filepath):
        try:
            df=pd.read_csv(filepath)
            return df
        except Exception as e:
            raise SensorException("Error occurred while data into dataframe")
    def transform_data(self):  
        try:
            training_df,testing_df=DataTransformer.read_data(self.datavalidationartifact.valid_train_path),DataTransformer.read_data(self.datavalidationartifact.valid_test_path)
            training_df=training_df.drop(self.drop_columns,axis=1)
            testing_df=testing_df.drop(self.drop_columns,axis=1)
        except Exception as e:
            raise SensorException("Error occurred while reading training and testing data")
        X_train,y_train=training_df.drop(target_col,axis=1),training_df[target_col]
        X_test,y_test=testing_df.drop(target_col,axis=1),testing_df[target_col]

        self.logger.log_message("Retrieved Training and Testing data")
        try:
            X_train=self.preprocessor_obj.fit_transform(X_train)
            X_test=self.preprocessor_obj.transform(X_test)
        except Exception as e:
            raise SensorException("Error occurred while preprocessing data")
        self.logger.log_message("Preprocessed Training and Testing data")
        X_train,y_train=self.smt.fit_resample(X_train,y_train)
        y_train=y_train.replace({'pos':1,'neg':0})
        y_test=y_test.replace({'pos':1,'neg':0})
        self.logger.log_message("Applied SMOTE for handling class imbalance")
        train=np.c_[X_train,np.array(y_train)]
        test=np.c_[X_test,np.array(y_test)]
        self.logger.log_message("Combined X and Y into one")
        try:

            save_numpy_array(self.datatransformationconfig.transformed_train_path,train)
            save_numpy_array(self.datatransformationconfig.transformed_test_path,test)
            save_object(self.datatransformationconfig.preprocessor_filepath,self.preprocessor_obj)
        except Exception as e:
            raise SensorException("Error occurred while saving transformed data and preprocessor object")
        self.logger.log_message("Sucessfully transformed and saved data")

        return DataTransformerArtifact(self.datatransformationconfig.transformed_train_path,self.datatransformationconfig.transformed_test_path,self.datatransformationconfig.preprocessor_filepath)











