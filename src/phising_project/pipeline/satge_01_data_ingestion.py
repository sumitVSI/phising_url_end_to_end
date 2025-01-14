from phising_project.logging import logger
from phising_project.config.configuration import ConfigurationManager
from phising_project.components.data_ingestion import DataIngestion



class DataIngestionTrainingPipeline:
        def __init__(self):
                pass
        
        def main(self):
            try:
                config = ConfigurationManager()
                data_ingestion_config = config.get_data_ingestion_config()
                data_ingestion = DataIngestion(config=data_ingestion_config)
                data_ingestion.download_zip_file()
                data_ingestion.extract_zip_file()
            except Exception as e:
                        raise e