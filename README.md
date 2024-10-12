# SensorFaultPrediction
Air pressure systems in cars help with important tasks like keeping the tires properly inflated for safety and fuel efficiency, making the engine run better by controlling the flow of air, and ensuring the car's comfort through air conditioning and suspension systems. For example, the **Tire Pressure Monitoring System (TPMS)** warns you when tire pressure is low, the **AC system** cools the car's interior, and **air suspension** adjusts the car's height for a smoother ride. These systems work together to make the car safer, more efficient, and more comfortable for driving. **Sensors** like pressure and flow sensors play a key role in monitoring and controlling these systems, ensuring that everything from tire inflation to engine performance and cabin comfort stays optimal, so you get the best driving experience.

In this project, we aim to classify whether a failure was caused by the APS system or not. By predicting this failure while the car is in motion, we can take precautionary actions to prevent accidents. Additionally, knowing beforehand that the APS system is not the cause of a problem can help save both time and repair costs when diagnosing issues.

## Technologies used

### Tech Stack

| Python                       | MongoDB                     | Apache Kafka                |
| ---------------------------- | --------------------------- | --------------------------- |
| ![Python](https://img.icons8.com/color/48/000000/python.png)  | ![MongoDB](https://img.icons8.com/ios/50/000000/mongodb.png)  | ![Apache Kafka](https://img.icons8.com/ios/50/000000/apache-kafka.png) |

| Docker                       | Flask                       | AWS                         |
| ---------------------------- | --------------------------- | --------------------------- |
| ![Docker](https://img.icons8.com/ios/50/000000/docker.png)  | ![Flask](https://img.icons8.com/ios/50/000000/flask.png)  | ![AWS](https://img.icons8.com/ios/50/000000/amazon-web-services.png) |

---

### Libraries

| NumPy                        | XGBoost                     | Matplotlib                  |
| ---------------------------- | --------------------------- | --------------------------- |
| ![NumPy]([https://img.icons8.com/ios/50/000000/numpy.png])  | ![XGBoost](https://img.icons8.com/ios/50/000000/xgboost.png)  | ![Matplotlib](https://img.icons8.com/ios/50/000000/matplotlib.png) |

| imbalanced-learn (imblearn)   |
| ---------------------------- |
| ![Imbalanced Learn](https://img.icons8.com/ios/50/000000/balance.png) |

---

### Infrastructure

| Amazon S3                    | Amazon EC2                  | Amazon ECR                  |
| ---------------------------- | --------------------------- | --------------------------- |
| ![Amazon S3](https://img.icons8.com/ios/50/000000/amazon-s3.png)  | ![Amazon EC2](https://img.icons8.com/ios/50/000000/amazon-ec2.png)  | ![Amazon ECR](https://img.icons8.com/ios/50/000000/amazon-ecr.png) |

| GitHub Actions               |
| ---------------------------- |
| ![GitHub Actions](https://img.icons8.com/ios/50/000000/github-actions.png) |

### Skills

| ETL (Extract, Transform, Load) | Data Analysis & Exploration | Machine Learning Model Development |
| ------------------------------ | ---------------------------- | ---------------------------------- |
| ![ETL](https://img.icons8.com/ios/50/000000/database-import.png)  | ![Data Analysis](https://img.icons8.com/ios/50/000000/data-analytics.png)  | ![ML](https://img.icons8.com/ios/50/000000/artificial-intelligence.png) |

## 

| CI/CD Pipelines               |
| ----------------------------- |
| ![CI/CD](https://img.icons8.com/ios/50/000000/automation.png) |

## Data Collection
The data is uploaded in batches through the Kafka producer, which reads CSV files in chunks of 200 records at a time using `pandas.read_csv()`. Each chunk is serialized into JSON format using Kafka's `JSONSerializer` and then sent as a batch to the specified Kafka topic. The producer uploads these records asynchronously, using the `produce()` function to push each batch of data, and polls Kafka to ensure non-blocking operations. Once a batch is processed, the producer flushes any remaining messages to ensure all data is uploaded. This batch processing ensures efficient handling of large datasets.

## Data Exploration


## Data Analysis


