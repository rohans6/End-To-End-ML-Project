from Sensor.Constant import training_pipeline
import os
from datetime import datetime
# Define Data Ingestion Configuration
class DataIngestionConfiguration:
    def __init__(self):
        self.project_dir=training_pipeline.project_directory
        self.artifact_dir=os.path.join(self.project_dir,training_pipeline.artifact_directory)
        self.feature_store=os.path.join(self.artifact_dir,training_pipeline.feature_store)
        self.ingested_dir=os.path.join(self.artifact_dir,training_pipeline.ingested_folder)
        self.sensor_file=os.path.join(self.feature_store,training_pipeline.sensor_file).replace("\\",'/')
        self.training_file=os.path.join(self.ingested_dir,training_pipeline.training_file).replace("\\",'/')
        self.testing_file=os.path.join(self.ingested_dir,training_pipeline.testing_file).replace("\\",'/')
        self.testing_split=training_pipeline.testing_split

# Define Data Validation Configuration
class DataValidationConfiguration:
    def __init__(self):
        self.project_dir=training_pipeline.project_directory
        self.artifact_dir=os.path.join(self.project_dir,training_pipeline.artifact_directory)
        self.datavalidation_folder=os.path.join(self.artifact_dir,training_pipeline.datavalidation_folder)
        self.valid_folder=os.path.join(self.datavalidation_folder,training_pipeline.valid_folder)
        self.invalid_folder=os.path.join(self.datavalidation_folder,training_pipeline.invalid_folder)
        self.drift_report_folder=os.path.join(self.datavalidation_folder,training_pipeline.drift_report_folder)
        self.drift_report_filepath=os.path.join(self.drift_report_folder,training_pipeline.drift_report_filename).replace("\\",'/')


# Define DataTransformation Configuration
class DataTransformerConfiguration:
    def __init__(self):
        self.project_dir=training_pipeline.project_directory
        self.artifact_dir=os.path.join(self.project_dir,training_pipeline.artifact_directory)
        self.datatransformation_folder=os.path.join(self.artifact_dir,training_pipeline.datatransformation_folder)
        self.transformed_train_path=os.path.join(self.datatransformation_folder,training_pipeline.transformed_train).replace("\\",'/')
        self.transformed_test_path=os.path.join(self.datatransformation_folder,training_pipeline.transformed_test).replace("\\",'/')
        self.preprocessor_filepath=os.path.join(self.datatransformation_folder,training_pipeline.preprocessor_obj).replace("\\",'/')

# Define ModelTraining Configuration
class ModelTrainerConfiguration:
    def __init__(self):
        self.project_dir=training_pipeline.project_directory
        self.artifact_dir=os.path.join(self.project_dir,training_pipeline.artifact_directory)
        self.modeltraining_folder=os.path.join(self.artifact_dir,training_pipeline.modeltraining_folder)
        self.trained_model_filepath=os.path.join(self.modeltraining_folder,training_pipeline.model_folder,training_pipeline.model_name).replace("\\",'/')

# Define ModelEvaluation Configuration
class ModelEvaluatorConfiguration:
    def __init__(self):
        self.threshold=0.5

# Define Model Pusher Configuration
class ModelPusherConfiguration:
    def __init__(self):
        self.project_dir=training_pipeline.project_directory
        self.artifact_dir=os.path.join(self.project_dir,training_pipeline.artifact_directory)
        self.saved_model_dir=os.path.join(self.project_dir,training_pipeline.saved_model_dir)
        self.timestamp=int(datetime.now().timestamp())
        self.timestamp_dir=os.path.join(self.saved_model_dir,str(self.timestamp))
        self.saved_model_file_path=os.path.join(self.timestamp_dir,training_pipeline.model_name)

        self.model_pusher_dir=os.path.join(self.artifact_dir,training_pipeline.model_pusher_dir)
        self.model_pusher_file_path=os.path.join(self.model_pusher_dir,training_pipeline.model_name)


        