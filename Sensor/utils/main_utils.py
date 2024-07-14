import os,sys
import yaml
from Sensor.exception import SensorException
from Sensor.logger import Logger
import numpy as np
import dill
import shutil
def read_yaml_file(filename):
    try:
        with open(filename, 'r') as file:
            config = yaml.safe_load(file)
        return config
    except Exception as e:
        raise SensorException(f"Error reading YAML file: {filename}. Error: {str(e)}")

def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.dump(content, file)
    except Exception as e:
        raise SensorException(e, sys)

def save_numpy_array(filepath, numpy_array):
    try:
        dir=os.path.dirname(filepath)
        if not os.path.exists(dir):
            os.makedirs(dir)
        with open(filepath,'wb') as file_object:
            np.save(file_object,numpy_array)
    except Exception as e:
        raise SensorException(f"Error saving numpy array to file: {filepath}. Error: {str(e)}")

def save_object(filepath,obj):
    try:
        dir=os.path.dirname(filepath)
        if not os.path.exists(dir):
            os.makedirs(dir)
        with open(filepath,'wb') as file_object:
            dill.dump(obj, file_object)
    except Exception as e:
        raise SensorException(f"Error saving object to file: {filepath}. Error: {str(e)}")

def load_numpy_array(filepath):
    try:
        with open(filepath,'rb') as file_object:
            return np.load(file_object,allow_pickle=True)
    except Exception as e:
        raise SensorException(f"Error loading numpy array from file: {filepath}. Error: {str(e)}")
def load_object(filepath):
    try:
        with open(filepath,'rb') as file_object:
            return dill.load(file_object)
    except Exception as e:
        raise SensorException(f"Error loading object from file: {filepath}. Error: {str(e)}")