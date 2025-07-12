import os
from datetime import date

# For MongoDB connection
DATABASE_NAME = "Proj1"
COLLECTION_NAME = "Proj1-Data"
MONGODB_URL_KEY = "MONGODB_URL"

PIPELINE_NAME: str = ""
ARTIFACT_DIR: str = 'artifact'

FILE_NAME: str = "data.csv"
TRAIN_FILE_NAME: str = 'train.csv'
TEST_FILE_NAME: str = 'test.csv'
SCHEMA_FILE_PATH = os.path.join('config','schema.yaml')       

"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str = "Proj1-Data"
DATA_INGESTION_DIR_NAME: str = 'data_ingestion'
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTION_DIR: str = "ingestion"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.25
