import os
from Sensor import *

project_directory=os.path.dirname(sensor_directory)
artifact_directory=os.path.join(project_directory,'Artifact')
data_validation=os.path.join(artifact_directory,'Data Validation')
validated=os.path.join(data_validation,'Validated')
invalid=os.path.join(data_validation,'Invalid')

