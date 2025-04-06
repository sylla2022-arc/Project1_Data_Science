from src.Project1_Data_Science.constants import *
from src.Project1_Data_Science.utils.common import read_yaml, create_directories
from src.Project1_Data_Science.entity.config_entity import (DataIngestionconfig, DataTransformationConfig, DataValidationConfig)

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
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir])
        data_transformation_config = DataTransformationConfig(
            root_dir=Path(config.root_dir),
            data_path=Path(config.data_path)
        )
        return data_transformation_config