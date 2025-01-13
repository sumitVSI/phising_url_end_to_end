import os
import sys
from datetime import datetime

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

ROOT_DIR = os.getcwd()
LOG_DIR_NAME = "logs"
LOG_FILE_NAME = F"log_{CURRENT_TIME_STAMP}.log"
LOG_DIR_PATH = os.path.join(ROOT_DIR,LOG_DIR_NAME)
LOG_FILE_NAME_PATH = os.path.join(LOG_DIR_PATH,LOG_FILE_NAME)