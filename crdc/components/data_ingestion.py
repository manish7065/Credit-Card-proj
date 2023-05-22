from crdc.logger import logging
from crdc.exception import CrdcException
from dataclasses import dataclass

import os,sys
import pandas as pd

@dataclass
class DataIngestionConfig:

    data_ingestion_path = os.path.join("data","default of credit card clients.xls")
    raw_data_path = os.path.join("artifact","raw.csv")

class DataIngestion:
    """
    Data will be collected from the source and stored to the feature store or artifact.
    """

    def  __init__(self) -> None:
        self.data_ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            logging.info(f"{'<'*10}Initiating Data Ingestion.{'>'*10}")
            df = pd.read_csv(os.path.join(self.data_ingestion_config.data_ingestion_path))
            
        except Exception as e:
            raise CrdcException(e,sys)