import os
from Sensor import *
project_directory=os.path.dirname(sensor_directory)
artifact_directory=os.path.join(project_directory,'Artifact')
feature_store=os.path.join(artifact_directory,'feature_store')
ingested=os.path.join(artifact_directory,'ingested')
sensor_file=os.path.join(feature_store,'sensor_data.csv')
training_file=os.path.join(ingested,'training_data.csv')
testing_file=os.path.join(ingested,'testing_data.csv')
testing_split=0.2
