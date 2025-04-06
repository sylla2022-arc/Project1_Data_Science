import os
import requests
import urllib.request  as request
from src.Project1_Data_Science import logger
from src.Project1_Data_Science.constants import *
from src.Project1_Data_Science.entity.config_entity import (DataValidationConfig)
import pandas as pd

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
        

    def validation_all_columns(self) -> bool:

        try:
            validation_status = None
            data = pd.read_csv(self.config.unzip_data)
            logger.info("Data loaded successfully for validation.")
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validaion status : {validation_status}")
                    logger.info(f"Column {col} is not in the schema.")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validaion status : {validation_status}")
                    logger.info(f"Column {col} is in the schema.")

            return validation_status
        
        except Exception as e:
            logger.exception("Error occurred during data validation.")
            raise e
         
