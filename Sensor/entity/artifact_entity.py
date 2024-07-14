from Sensor.Constant import training_pipeline
import os
from dataclasses import dataclass

# Define Data Ingestion Artifact
@dataclass
class DataIngestionArtifact: 
    training_file: str
    testing_file:str

# Define Data Validation Artifact
@dataclass
class DataValidationArtifact:
    validation_status:bool
    valid_train_path:str
    valid_test_path:str
    invalid_train_path:str
    invalid_test_path:str
    drift_report:str

# Define Data Transformation Artifact
@dataclass
class DataTransformerArtifact:
    transformed_train_path:str
    transformed_test_path:str
    preprocessing_obj:str

# Define Model Training Artifact
@dataclass
class ModelTrainerArtifact:
    trained_model_path:str
    classification_report: dict

# Define Model Evaluation Artifact:
@dataclass
class ModelEvaluatorArtifact:
    is_model_accepted:bool
    best_model_path:str
    trained_model_path:str

# Define Model Pusher Artifact
@dataclass
class ModelPusherArtifact:
    pushed_model_path:str
    saved_model_path:str