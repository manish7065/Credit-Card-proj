from crdc.logger import logging 
from crdc.exception import CrdcException
from dataclasses import dataclass
import os,sys
import pandas as pd
import numpy as np



@dataclass
class DataTransformationConfig:
    transformed_data_file_path = os.path.join("artfact",'transformed_data.csv')
    raw_data_file_path = os.path.join('artifact','raw.csv')

class DataTransformation():
    def  __init__(self) -> None:
        self.data_transformation_config = DataTransformationConfig()

    def initiate_data_transformation(self):
        try:
            logging.info(f"{'<<'*10} Initiating Data Transformation. {'>>'*10}")
            raw_data_file_path=self.data_transformation_config.raw_data_file_path
            raw_data = pd.read_csv(raw_data_file_path)

            # removing 'ID' column
            df=raw_data.drop(['ID'],axis=1)
            
            # Function to remove outlier
            def remove_outliers_zscore(data, column, threshold=3):
                z_scores = (data[column] - np.mean(data[column])) / np.std(data[column])
                outliers = np.abs(z_scores) > threshold
                cleaned_data = data[~outliers]
                return cleaned_data
            # Removing outlier in 
            df = remove_outliers_zscore(df,'LIMIT_BAL')
            transformed_data_file_path=self.data_transformation_config.transformed_data_file_path
            os.makedirs(os.path.dirname(transformed_data_file_path),exist_ok=True)
            
            logging.info(f"saving new transformed Data to {transformed_data_file_path}")
            
            df.to_csv(transformed_data_file_path,header=True)
            logging.info(f"{'<<'*10}  Data Transformation sucessfully completed. {'>>'*10}")

        except Exception as e:
            raise CrdcException(e,sys)

        
