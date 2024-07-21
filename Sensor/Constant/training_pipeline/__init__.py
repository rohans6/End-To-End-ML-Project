import os
#from Sensor import *

# Global variables
testing_split=0.2
target_col='class'
train_file='training.csv'
test_file='test.csv'

# Define project directory
#project_directory=os.path.dirname(sensor_directory)
#log_dir=os.path.join(project_directory,'Logs')
log_dir='Logs'
artifact_dir='Artifact'
config_dir='config'

# Define folders for Data Ingestion
data_ingestion_folder='DataIngestion'
#artifact_directory='Artifact'
feature_store='feature_store'
ingested_folder='ingested'
sensor_file='sensor_data.csv'
training_file='training_data.csv'
testing_file='testing_data.csv'
testing_split=0.2

# Define folders for Data Validation
data_validation_folder='DataValidation'
valid_folder='valid'
invalid_folder='invalid'
#schema_file=os.path.join(project_directory,'config','schema.yaml')
schema_file=os.path.join(config_dir,'schema.yaml')
drift_report_folder='drift_report'
drift_report_filename='report.yaml'

# Define folders for Data Transformation
data_transformation_folder='Data_transformation'
transformed_train='train.npy'
transformed_test='test.npy'
preprocessor_obj='preprocessor.pkl'
knearest_neighbors=5
resampling_strategy=0.05

# Define folders for Model Training
model_training_folder='Model_training'
model_folder='trained_model'
model_name='model.pkl'


# Define folders for Model Evaluation
model_evaluator_folder='Model_Evaluator'

# Define folders for Model pusher
saved_model_dir=os.path.join('saved_models')
model_pusher_dir='Model_pusher'

# define folders for training
pipeline_name='sensor'