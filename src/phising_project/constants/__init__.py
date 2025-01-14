import os
import sys
from datetime import datetime
from pathlib import Path

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

ROOT_DIR = os.getcwd()
LOG_DIR_NAME = "logs"
LOG_FILE_NAME = F"log_{CURRENT_TIME_STAMP}.log"
LOG_DIR_PATH = os.path.join(ROOT_DIR,LOG_DIR_NAME)
LOG_FILE_NAME_PATH = os.path.join(LOG_DIR_PATH,LOG_FILE_NAME)

## config files
CONFIG_FOLDER_NAME = "config"
CONFIG_FILE_NAME = "config.yaml"
SCHEMA_FILE_NAME = "schema.yaml"
PARAMETER_FILE_NAME = "params.yaml"

CONFIG_FILE_PATH = Path(os.path.join(ROOT_DIR,CONFIG_FOLDER_NAME,CONFIG_FILE_NAME))
SCHEMA_FILE_PATH = Path(os.path.join(ROOT_DIR,CONFIG_FOLDER_NAME,SCHEMA_FILE_NAME))
PRAMETER_FILE_PATH = Path(os.path.join(ROOT_DIR,CONFIG_FOLDER_NAME,PARAMETER_FILE_NAME))

## Data Ingestion

DATA_INGESTION_CONFIG_KEY = "data_ingestion_config"
DATA_INGESTION_DIR_KEY = "root_dir_name"
DATA_INGESTION_DOWNLOAD_URL_KEY = "data_set_url"
DATA_INGESTION_RAW_DATA_STORE_KEY = "local_data_path"
DATA_INGESTION_UNZIP_DATA_STORE_KEY = "unzip_data_path"