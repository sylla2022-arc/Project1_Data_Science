
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from src.Project1_Data_Science import logger
from src.Project1_Data_Science.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.Project1_Data_Science.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.Project1_Data_Science.config.configuration import ConfigurationManager
from src.Project1_Data_Science.pipeline.model_evaluation_pipeline import ModelEvaluationTrainingPipeline
from src.Project1_Data_Science.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.Project1_Data_Science.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline


logger.info("Bienvenue dans mon projet de data science !")
# data ingestion pipeline
# This is the main entry point for the data science project.
STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f"{'>>' * 10} {STAGE_NAME} started {'<<' * 10}")
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f"{'>>' * 10} {STAGE_NAME} completed {'<<' * 10}")

except Exception as e:
    logger.exception(e)
    raise e

# data validation pipeline
# This is the main entry point for the data validation pipeline.
STAGE_NAME = "Data Validation stage"
try:
    logger.info(f"{'>>' * 10} {STAGE_NAME} started {'<<' * 10}")
    obj = DataValidationTrainingPipeline()
    obj.initiate_data_validation()
    logger.info(f"{'>>' * 10} {STAGE_NAME} completed {'<<' * 10}")

except Exception as e:
    logger.exception(e)
    raise e

# data transformation pipeline
# This is the main entry point for the data transformation pipeline.
STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f"{'>>' * 10} {STAGE_NAME} started {'<<' * 10}")
    obj = DataTransformationTrainingPipeline()
    obj.initiate_data_transformation()
    logger.info(f"{'>>' * 10} {STAGE_NAME} completed {'<<' * 10}")

except Exception as e:
    logger.exception(e)
    raise e

# model trainer pipeline
# This is the main entry point for the model trainer pipeline.
STAGE_NAME = "Model Trainer stage"
try:
    logger.info(f"{'>>' * 10} {STAGE_NAME} started {'<<' * 10}")
    obj = ModelTrainerTrainingPipeline()
    obj.initiate_model_training()
    logger.info(f"{'>>' * 10} {STAGE_NAME} completed {'<<' * 10}")

except Exception as e:
    logger.exception(e)
    raise e

# model evaluation pipeline
# This is the main entry point for the model evaluation pipeline.
STAGE_NAME = "Model Evaluation stage"
try:
    logger.info(f"{'>>' * 10} {STAGE_NAME} started {'<<' * 10}")
    obj = ModelEvaluationTrainingPipeline()
    obj.initiate_model_evaluation()
    logger.info(f"{'>>' * 10} {STAGE_NAME} completed {'<<' * 10}")
except Exception as e:
    logger.exception(e)
    raise e
