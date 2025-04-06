from src.Project1_Data_Science.config.configuration import ConfigurationManager
from src.Project1_Data_Science.components.data_validation import DataValidation
from src.Project1_Data_Science import logger


STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_validation(self) -> None:
        """Method to start the data validation process"""
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(data_validation_config)
        data_validation.validation_all_columns()
        logger.info("Data validation completed successfully.")
       

    
if __name__ == "__main__":
    try:
        logger.info(f"{'>>' * 10} {STAGE_NAME} started {'<<' * 10}")
        obj = DataValidationTrainingPipeline()
        obj.initiate_data_validation()
        logger.info(f"{'>>' * 10} {STAGE_NAME} completed {'<<' * 10}")

    except Exception as e:
        logger.exception(e)
        raise e
       