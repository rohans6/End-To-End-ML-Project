
# Define two types of configurations one for schema registry and another for Kafka 

kafka_config = {
    'bootstrap.servers': 'pkc-12576z.us-west2.gcp.confluent.cloud:9092',
    'security.protocol': 'SASL_SSL',  # Optional, depending on your security setup
    'sasl.mechanisms': 'PLAIN',       # Optional, depending on your security setup
    'sasl.username': 'OHLXG66PJJDAOZTA', # Optional, depending on your security setup
    'sasl.password': 'H+w0JfC59R/oVMcADBF7e7rEeiR6XdXTsdZtlA4gXSrbUudQoFrOA2ol5O/zl9HS', # Optional, depending on your security setup
    'compression.type' :'gzip', # Optional, depending on your security setup
    'batch.size': 16384
}

schema_config={
    'url':'https://psrc-57o65q.us-west2.gcp.confluent.cloud',
    'basic.auth.user.info': "XMZXIFFUPFIQUZB5:pIenb1hEqN4AY6GlpmnHbCn26bkAG9ayv+QmUCvWPbsM+GNh08gnyPRSK1ov2rIe"
}

print(schema_config)
print(kafka_config)

# Creating schema string
data_dir='D:\DataScience\Projects\SensorProject\End-To-End-ML-Project\Data'
sample_topic=os.listdir(data_dir)[0]
sample_file=os.path.join(data_dir,sample_topic,os.listdir(os.path.join(data_dir,sample_topic))[0])

with open(sample_file,'r') as file_object:
    columns=file_object.readline().strip().split(',')
item_schema = {
    "type": "object",
    "properties": {},
    "required": columns
}

for column in columns:
    item_schema["properties"][column] = {"type": "string","description": "This is a string"}
schema_string={ "$id": "http://example.com/myURI.schema.json",
            "$schema": "http://json-schema.org/draft-07/schema#",
            "type":"array",
            "items":item_schema,
            #"additionalProperties": False,
            "description": "Schema for batch of records",
            #"properties": dict(),
            "title": "SampleRecord",
            #"type": "object"
            }
#for column in columns:
    #schema_string['properties'].update({column: {"type": "string","description": "This is a string"}})
schema_string=json.dumps(schema_string)
print(schema_string)
