from pathlib import Path
from src.Project1_Data_Science.config.configuration import ConfigurationManager
from src.Project1_Data_Science.components.data_transformation import DataTransformation
from src.Project1_Data_Science import logger


STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self) -> None:
        """Method to start the data transformation process"""
        try:
            with( open(Path("artifacts/data_validation/status.txt"))) as file:
                status = file.read().split(" ")[-1]
                if status.strip() == "True":
                    config = ConfigurationManager()
                    data_transmation_config = config.get_data_transformation_config()
                    data_transformation = DataTransformation(config=data_transmation_config)
                    data_transformation.split_data()
                    logger.info(f"Data transformation completed.")
                else:
                    raise Exception(f"Data validation failed (See data Schema). Data transformation skipped.")
        except Exception as e:
            logger.exception(e)
            raise e
        