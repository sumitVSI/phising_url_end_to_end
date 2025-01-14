import os
import urllib.request as request
import zipfile
from phising_project.logging import logger
from phising_project.utils.common import *
from phising_project.entity import DataIngestionConfiguration

class DataIngestion:
    def __init__(self, config:DataIngestionConfiguration):
        self.config = config

    def download_zip_file(self):
        try:
            zip_file_name = os.path.basename(self.config.data_set_url)
            zip_file_path = os.path.join(self.config.local_data_path,zip_file_name)
            self.zip_file_path_ = zip_file_path
            if not os.path.exists(zip_file_path):
                filename, headers = request.urlretrieve(
                    url = self.config.data_set_url,
                    filename=zip_file_path
                )
                logger.info(f"{filename} downloaded! with following info: \n{headers}")
            else:
                logger.info(f"File already exists of size: {get_size(self.config.local_data_path)}")
        except Exception as e:
            raise e

    def extract_zip_file(self):
        try:
            unzip_path = self.config.unzip_data_path
            with zipfile.ZipFile(self.zip_file_path_,'r') as zip_file:
                zip_file.extractall(unzip_path)
        except Exception as e:
            raise e