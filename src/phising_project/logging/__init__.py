import os
import logging
from phising_project.constants import *

os.makedirs(LOG_DIR_PATH,exist_ok=True)

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

logging.basicConfig(level=logging.INFO,
                    format=logging_str,
                    handlers=[logging.FileHandler(LOG_FILE_NAME_PATH),logging.StreamHandler(sys.stdout)])

logger = logging.getLogger("phising_projectLogger")