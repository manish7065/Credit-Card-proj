from crdc.components.data_ingestion import DataIngestion

di=DataIngestion()

idi=di.initiate_data_ingestion()
print(f"data stored:{idi}")