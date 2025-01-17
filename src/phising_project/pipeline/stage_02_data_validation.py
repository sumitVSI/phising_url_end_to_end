from phising_project.logging import logger
from phising_project.config.configuration import ConfigurationManager
from phising_project.components.data_validation import DataValidation

class DataValidationTrainingPipeline:
        def __init__(self):
                pass
        
        def main(self):
            try:
                config = ConfigurationManager()
                data_ingestion_config = config.get_data_ingestion_config()
                data_validation_config = config.get_data_validation_configuration()
                data_validation = DataValidation(ingestion_config=data_ingestion_config,config=data_validation_config)
                data_validation.file_exist_validation()
                data_validation.number_of_columns_validation()
                data_validation.datatype_of_columns_validation()
                data_validation.null_value_of_columns_validation()
            except Exception as e:
                        raise e