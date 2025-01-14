from phising_project.logging import logger
from phising_project.pipeline.satge_01_data_ingestion import DataIngestionTrainingPipeline

##logger.info("checking the log file after changing date time format") #checking of loogging files

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<<<<<<<<")
    logger.info("x===========================================================================x")
except Exception as e:
    logger.exception(e)
    raise e