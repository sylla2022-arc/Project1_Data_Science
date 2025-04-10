from src.Project1_Data_Science.config.configuration import ConfigurationManager
from src.Project1_Data_Science.components.model_evaluation import ModelEvaluation
from src.Project1_Data_Science import logger


STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self) -> None:
        """Method to start the model evaluation process"""
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(model_evaluation_config)
        model_evaluation_config.log_into_mlflow()
        logger.info(f"{STAGE_NAME} completed successfully.")