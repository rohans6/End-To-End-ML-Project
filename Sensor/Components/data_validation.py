from Sensor.Constant.data_ingestion_config import *
from Sensor.entity.config_entity import DataValidationConfiguration
from Sensor.entity.artifact_entity import DataValidationArtifact
from Sensor.Constant.training_pipeline import schema_file,log_dir
import pandas as pd
import os,sys
from Sensor.exception import SensorException
from Sensor.logger import Logger
from Sensor.utils.main_utils import read_yaml_file
from scipy.stats import ks_2samp
import shutil
from Sensor.utils.main_utils import write_yaml_file
class DataValidation:
    def __init__(self,dataingestionartifact,datavalidationconfig):
        try:

            self.dataingestionartifact=dataingestionartifact
            self.datavalidationconfig=datavalidationconfig
            self.__schema_file=read_yaml_file(schema_file)
            self.logger=Logger(log_dir,'DataValidation.log')
        except Exception as e:
            raise SensorException("Error occurred while reading schema file")
    def validate_number_columns(self,df):
        try:
            if len(self.__schema_file['columns'])==df.shape[1]:
                self.logger.log_message("The columns in the dataframe match with the schema file")
                return True
            self.logger.log_message("The columns in the dataframe does not match with the schema file")
            return False
        except Exception as e:
            SensorException('Error occured while validating number of columns')
    def validate_column_names(self,df):    
        try:
            schema_cols=self.__schema_file['numerical_columns']
            df_cols=df.columns
            flag=True
            missing_columns=[]
            for col in schema_cols:
                if col not in df_cols:
                    flag=False
                    missing_columns.append(col)
            self.logger.log_message(f"Columns missing in dataframe are :- {missing_columns}")
            return flag
        except Exception as e:
            raise SensorException("Error occurred while validating column names")

    @staticmethod
    def read_csv(filepath):
        try:
            df=pd.read_csv(filepath)
            return  df
        except Exception as e:
            raise SensorException("Error occurred while reading file into dataframe")

    def detect_covariance_shift(self,df1,df2,threshold=0.05):
        report={}
        try:
            is_shift= False
            for col in df1.columns:
                col1=df1[col]
                col2=df2[col]
                result=ks_2samp(col1,col2)
                if result.pvalue>threshold:
                    is_shift=True
                    self.logger.log_message(f"Covariance shift detected in column: {col}")
                report.update({col:[result.pvalue,is_shift]})
            try:
                if not os.path.exists(os.path.dirname(self.datavalidationconfig.drift_report_filepath)):
                    os.mkdir(self.datavalidationconfig.drift_report_folder)
                else:
                    shutil.rmtree(self.datavalidationconfig.drift_report_filepath)
                write_yaml_file(self.datavalidationconfig.drift_report_filepath,report,True)
                self.logger.log_message("Drift report written successfully")
            except Exception as e:
                raise SensorException("Error occured while writing drift report")
            return is_shift
            
        except Exception as e:
            raise SensorException("Error occurred while detecting covariance shift")

    def validate_data(self):
        try:
            training_df,testing_df=DataValidation.read_csv(self.dataingestionartifact.training_file),DataValidation.read_csv(self.dataingestionartifact.testing_file)
        except Exception as e:
            raise SensorException("Error occurred while reading training and testing data")
        if not self.validate_number_columns(training_df):
            raise SensorException("Number of columns in training data do not match the schema file")
        if not self.validate_number_columns(testing_df):
            raise SensorException("Number of columns in testing data do not match the schema file")
        if not self.validate_column_names(training_df):
            raise SensorException("Column names in training data do not match the schema file")
        if not self.validate_column_names(testing_df):
            raise SensorException("Column names in testing data do not match the schema file")
        if os.path.exists(self.datavalidationconfig.datavalidation_folder):
            shutil.rmtree(self.datavalidationconfig.datavalidation_folder)
        os.makedirs(self.datavalidationconfig.datavalidation_folder)
        drift_status=self.detect_covariance_shift(training_df,testing_df)

        return DataValidationArtifact(drift_status,self.dataingestionartifact.training_file,self.dataingestionartifact.testing_file,None,None,self.datavalidationconfig.drift_report_filepath)
