from src.Project1_Data_Science.constants import *
from src.Project1_Data_Science.utils.common import read_yaml, create_directories, save_json
from src.Project1_Data_Science.entity.config_entity import (DataIngestionconfig, DataTransformationConfig, DataValidationConfig, ModelEvaluationConfig, ModelTrainerConfig)

class ConfigurationManager:
    def __init__(self, 
                 config_filepath: str = CONFIG_FILE_PATH,
                 params_filepath: str = PARAMS_FILE_PATH,
                 schema_filepath: str = SCHEMA_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        print(f"Type of artifacts_root: {type(self.config.artifacts_root)}")
        print(f"Value of artifacts_root: {self.config.artifacts_root}")


        create_directories([self.config.artifacts_root])
    # Data Ingestion Config
    def get_ingestion_config(self) -> DataIngestionconfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        dataingestion_config = DataIngestionconfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return dataingestion_config

# Data Validation Config
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema= self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
        root_dir=config.root_dir,
        STATUS_FILE=config.STATUS_FILE,
        unzip_data=config.unzip_data_dir,  
        all_schema=schema,
        )           
        return data_validation_config
    
    # Data Transformation Config
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir])
        data_transformation_config = DataTransformationConfig(
            root_dir=Path(config.root_dir),
            data_path=Path(config.data_path)
        )
        return data_transformation_config
    
    # Model Trainer Config
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN

        # Ensure the artifacts root directory exists
       
        create_directories([config.root_dir])


        # Create the model trainer config
        model_trainer_config = ModelTrainerConfig(
            root_dir= config.root_dir,
            train_data_path= config.train_data_path,
            test_data_path= config.test_data_path,
            model_name= config.model_name,
            alpha=params.alpha,
            random_state=params.random_state,
            l1_ratio=params.l1_ratio,
            target_column= schema.name
        )
        
        return model_trainer_config

    # ModelEvaluation Config
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir= config.root_dir,
            test_data_path= config.test_data_path,
            model_path= config.model_path,
            metric_file_name= config.metric_file_name,

            TARGET_COLUMN= schema.name,
            mlflow_uri= "https://dagshub.com/lassoinadame2018/Project1_Data_Science.mlflow",
            all_params= params
        )
        return model_evaluation_config