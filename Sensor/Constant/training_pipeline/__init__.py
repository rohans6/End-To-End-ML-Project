import os
from Sensor import *

# Global variables
testing_split=0.2
target_col='class'

# Define project directory
project_directory=os.path.dirname(sensor_directory)
log_dir=os.path.join(project_directory,'Logs')

# Define folders for Data Ingestion
artifact_directory='Artifact'
feature_store='feature_store'
ingested_folder='ingested'
sensor_file='sensor_data.csv'
training_file='training_data.csv'
testing_file='testing_data.csv'
testing_split=0.2

# Define folders for Data Validation
datavalidation_folder='DataValidation'
valid_folder='valid'
invalid_folder='invalid'
schema_file=os.path.join(project_directory,'config','schema.yaml')
drift_report_folder='drift_report'
drift_report_filename='report.yaml'

# Define folders for Data Transformation
datatransformation_folder='DataTransformation'
transformed_train='train.npy'
transformed_test='test.npy'
preprocessor_obj='preprocessor.pkl'
knearest_neighbors=5
resampling_strategy=0.04

# Define folders for Model Training
modeltraining_folder='ModelTraining'
model_folder='trained_model'
model_name='model.pkl'


# Define folders for Model Evaluation


# Define folders for Model pusher
saved_model_dir=os.path.join('saved_models')
model_pusher_dir='model_pusher'
