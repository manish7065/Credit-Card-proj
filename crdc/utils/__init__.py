from crdc.logger import logging
from crdc.exception import CrdcException
import os,sys
import yaml
import dill 

def read_yaml_file(file_path:str):
    try:
        with open(file_path,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise CrdcException(e,sys)
    
def save_object(file_path:str,obj:str):
    try:
        logging.info(f"Saving the file {obj} on path {file_path}")
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)
        logging.info(f"{obj} sucessfully saved at {file_path}.")
    except Exception as e:
        raise CrdcException(e,sys)

def load_obj(file_path:str):
    try:
        logging.info(f"loading object fron {file_path}.")

        if not os.path.exists(file_path):
            raise Exception(f"The file: {file_path} dosen't exist.")
        
        with open(file_path,"rb") as file_obj:
            return dill.load(file_obj)
        
    except Exception as e:
        raise CrdcException(e,sys)
