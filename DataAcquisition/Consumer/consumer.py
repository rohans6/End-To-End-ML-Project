# Necessary imports
from confluent_kafka import Consumer
from confluent_kafka.serialization import SerializationContext, MessageField
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.json_schema import JSONDeserializer
from confluent_kafka.serialization import Deserializer
import mysql.connector.cursor
import pandas as pd
import numpy as np
import os
import sys
sys.path.append('D:\DataScience\Projects\SensorProject\End-To-End-ML-Project')
from DataAcquisition.Confg import *
from DataAcquisition.Database import sql
from DataAcquisition.Database import mongodb
from uuid import uuid4
import logging
import mysql.connector
import shutil


# Remove previous Logs
if os.path.exists("DataAcquisition\Logs\\consumer.log"):
    os.remove("DataAcquisition\Logs\\consumer.log")

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.FileHandler("DataAcquisition\Logs\consumer.log"),
        logging.StreamHandler()
    ]
)

# Consume data from Kafka
kafka_config.update({'group.id':'group_consumer2','auto.offset.reset': 'earliest','enable.auto.commit':False})
consumer=Consumer(kafka_config)
json_deserializer=JSONDeserializer(schema_string)
for topic in os.listdir('Data'):    
    consumer.subscribe([topic])

    # Creating Database object
    db_obj=mongodb.MongoDb()
    none_counter=0
    #i,j=0,0
    #records=[]
    first_batch=True
    while True:
        try:
            msg=consumer.poll(1.0)
            if msg is None:
                none_counter+=1
                if none_counter>20:
                    break
                continue
            else:
                none_counter=0
                data=json_deserializer(msg.value(), SerializationContext(msg.topic(),MessageField.VALUE))
                logging.info(f'Received message: {msg.key()}')

                if first_batch:
                    columns=list(data[0].keys())
                    db_obj.create('sensorfaultprediction')
                    first_batch=False
                db_obj.insert_many([record for record in data])

                # Store data in my sql database
                #if i==0:
                    #columns,values=list(data.keys()),list(data.values())
                    #i+=1
                    #sql_obj.create_table(columns)
                #records.append(tuple(data.values()))
                #j+=1
                #if j>30:
                    #sql_obj.add_many(records)
                    #j=0
                    #records=[]

        except KeyboardInterrupt:
            break
    db_obj.close()

# Close the consumer
consumer.close()