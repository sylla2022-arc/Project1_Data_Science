from src.Project1_Data_Science import logger
from src.Project1_Data_Science.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.Project1_Data_Science.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.Project1_Data_Science.config.configuration import ConfigurationManager

logger.info("Bienvenue dans mon projet de data science !")

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f"{'>>' * 10} {STAGE_NAME} started {'<<' * 10}")
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f"{'>>' * 10} {STAGE_NAME} completed {'<<' * 10}")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"
try:
    logger.info(f"{'>>' * 10} {STAGE_NAME} started {'<<' * 10}")
    obj = DataValidationTrainingPipeline()
    obj.initiate_data_validation()
    logger.info(f"{'>>' * 10} {STAGE_NAME} completed {'<<' * 10}")

except Exception as e:
    logger.exception(e)
    raise e