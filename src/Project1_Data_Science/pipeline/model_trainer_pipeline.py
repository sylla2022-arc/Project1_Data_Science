from src.Project1_Data_Science.config.configuration import ConfigurationManager
from src.Project1_Data_Science.components.model_trainer import ModelTrainer
from src.Project1_Data_Science import logger


STAGE_NAME = "Model Trainer stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_training(self) -> None:
        """Method to start the model trainer process"""
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(model_trainer_config)
        model_trainer_config.train()
        logger.info(f"{STAGE_NAME} completed successfully.")
    
       