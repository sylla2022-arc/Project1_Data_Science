from src.Project1_Data_Science.config.configuration import ConfigurationManager
from src.Project1_Data_Science.components.data_ingestion import DataIngestion
from src.Project1_Data_Science import logger


STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self) -> None:
        """Method to start the data ingestion process"""
        config = ConfigurationManager()
        data_ingestion_config = config.get_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

    

if __name__ == "__main__":
    try:
        logger.info(f"{'>>' * 10} {STAGE_NAME} started {'<<' * 10}")
        obj = DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f"{'>>' * 10} {STAGE_NAME} completed {'<<' * 10}")

    except Exception as e:
        logger.exception(e)
        raise e
       