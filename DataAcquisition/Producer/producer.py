# Necessary imports
from confluent_kafka import Producer
from confluent_kafka.serialization import SerializationContext, MessageField
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.json_schema import JSONSerializer
from confluent_kafka.serialization import StringSerializer
import pandas as pd
import numpy as np
import os
import sys
sys.path.append('D:\DataScience\Projects\SensorProject\End-To-End-ML-Project')
from DataAcquisition.Confg import *
from uuid import uuid4
import logging
import shutil

# REQUIRED CONFIGURATIONS
data_dir="Data"
schemaregistryclient=SchemaRegistryClient(schema_config)
json_serializer=JSONSerializer(schema_string,schemaregistryclient)
string_serializer = StringSerializer('utf_8')
producer=Producer(kafka_config)

# Remove previous Logs
if os.path.exists("DataAcquisition\Logs"):
    shutil.rmtree("DataAcquisition\Logs")
    os.mkdir("DataAcquisition\Logs")
# Callback function
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.FileHandler("DataAcquisition\Logs\producer.log"),
        logging.StreamHandler()
    ]
)

# Callback function to handle delivery reports.
def callback_function(error,message):
    if error is not None:
        logging.info(f"Error occured for record: {message.value} Error:{error}")
        return 
    else:
        logging.info(f"Record Successfully Produced:{message.key()}")

# Produce data to Kafka
for topic in os.listdir(data_dir):
    for file in os.listdir(os.path.join(data_dir,topic)):
        file_path=os.path.join(data_dir,topic,file)
        for chunk in pd.read_csv(file_path,chunksize=1000):
            records=chunk.astype(str).to_dict(orient='records')
            for record in records:
                producer.produce(topic=topic,key=string_serializer(str(uuid4()), record),value=json_serializer(record,SerializationContext(topic,MessageField.VALUE)),on_delivery=callback_function)
                producer.poll(1.0)

#Flushing data
producer.flush()






        

        