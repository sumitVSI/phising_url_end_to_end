from phising_project.constants import *
from phising_project.utils.common import *
from phising_project.entity import DataIngestionConfiguration

class ConfigurationManager:

    def __init__(self,
                 config_file_path = CONFIG_FILE_PATH,
                 schema_file_path = SCHEMA_FILE_PATH,
                 parameter_file_path = PRAMETER_FILE_PATH):
        try:
            self.config = read_yaml_file(config_file_path)
            self.schema = read_yaml_file(schema_file_path)
            self.params = read_yaml_file(parameter_file_path)
            self.artficats_dir_name = self.config.artifacts_dir_name
            create_directories([self.config.artifacts_dir_name])

            logger.info(f"Artifacts directory created at : {self.config.artifacts_dir_name}")
        
        except Exception as e:
            raise e
        
    def get_data_ingestion_config(self) -> DataIngestionConfiguration:

        try:
            config = self.config.data_ingestion_config

            data_ingestion_dir = Path(os.path.join(self.artficats_dir_name,config.root_dir_name))
            create_directories([data_ingestion_dir])

            raw_data_dir = Path(os.path.join(data_ingestion_dir,config.local_data_path))
            create_directories([raw_data_dir])

            unzip_data_dir = Path(os.path.join(data_ingestion_dir,config.unzip_data_path))
            create_directories([unzip_data_dir])

            data_ingestion_config = DataIngestionConfiguration(
                root_dir_name = data_ingestion_dir,
                data_set_url = config.data_set_url,
                local_data_path = raw_data_dir,
                unzip_data_path = unzip_data_dir 
            )

            logger.info(f"Data ingestion configuration updated: {data_ingestion_config}")

            return data_ingestion_config
        
        except Exception as e:
            raise e