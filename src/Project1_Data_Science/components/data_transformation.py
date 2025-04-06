import os
from sklearn.model_selection import train_test_split
from src.Project1_Data_Science import logger
from src.Project1_Data_Science.constants import *
from src.Project1_Data_Science.entity.config_entity import (DataTransformationConfig)
import pandas as pd

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
# Note : We can add different transformation methods here like scaling, encoding, etc.
    def split_data(self) -> None:
        logger.info("Splitting data into train and test sets.")
        data = pd.read_csv(self.config.data_path) # Load the data from the specified path in yaml config
        # Assuming the target variable is 'quality' and we want to predict it
        train_set, test_set = train_test_split(data, test_size=0.2, random_state=42)
        
        train_set.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test_set.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
        
        print(f"Train set shape: {train_set.shape}")
        print(f"Test set shape: {test_set.shape}")

        logger.info("Data splitting completed.")
        logger.info(train_set.shape)
        logger.info(test_set.shape)
    # You can add more transformation methods here as needed