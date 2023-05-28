from crdc.logger import logging
from crdc.exception import CrdcException
from dataclasses import dataclass

import os,sys
import pandas as pd

@dataclass
class DataIngestionConfig:

    data_ingestion_path = os.path.join("data","default of credit card clients.xls")

    artifact_dir = os.path.join("artifact")

class DataIngestion:
    """
    Data will be collected from the source and stored to the feature store or artifact.
    """

    def  __init__(self) -> None:
        self.data_ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            logging.info(f"{'<'*10}Initiating Data Ingestion.{'>'*10}")

            #Reading excel file from dat folder (can be changed letter if data ingestion path changes)
            data_ingestion_file_path =os.path.join(self.data_ingestion_config.data_ingestion_path)
            print(f"Data Ingestion path:{data_ingestion_file_path}")
            df = pd.read_excel(data_ingestion_file_path,header=1)

            # writing dataframe in csv format for easy read
            raw_data_dir=self.data_ingestion_config.artifact_dir
            print(f"Raw Data Dir:{raw_data_dir}")
            os.makedirs(raw_data_dir,exist_ok=True)
            raw_data_file_path=os.path.join(raw_data_dir,"raw.csv")
            
            df.to_csv(raw_data_file_path)

            logging.info(f"{'<'*10}Data ingestion sucessfully completed.{'>'*10}")
            return raw_data_file_path
            
        except Exception as e:
            raise CrdcException(e,sys)