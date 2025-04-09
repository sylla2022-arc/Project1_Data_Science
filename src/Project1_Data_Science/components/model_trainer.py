import pandas as pd
import os
from src.Project1_Data_Science.entity.config_entity import ModelTrainerConfig
from src.Project1_Data_Science import logger
from sklearn.linear_model import ElasticNet
import joblib

class ModelTrainer :
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
    
    def train(self):
        logger.info(f"Training model with config: {self.config}")
        
        # Load training data
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        # Separate features and target
        X_train = train_data.drop(columns=[self.config.target_column])
        X_test = test_data.drop(columns=[self.config.target_column])

        y_train = train_data[[self.config.target_column]]

        y_test = test_data[[self.config.target_column]]

        # Train the model
        model_en = ElasticNet(
            alpha=self.config.alpha,
            random_state=self.config.random_state,
            l1_ratio=self.config.l1_ratio
        )
        
        model_en.fit(X_train, y_train)

        # Save the model
        model_path = os.path.join(self.config.root_dir, self.config.model_name)
        joblib.dump(model_en, model_path)
        
        logger.info(f"Model saved at: {model_path}")