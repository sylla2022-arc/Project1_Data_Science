from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionconfig :
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: Path
    unzip_data: Path
    all_schema: dict

@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path

@dataclass
class ModelTrainerConfig:
    root_dir : Path
    train_data_path: Path
    test_data_path: Path
    model_name : str
    alpha : float
    random_state : int
    l1_ratio : float
    target_column : str

@dataclass
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    metric_file_name: Path
    TARGET_COLUMN : str
    mlflow_uri: str
    all_params : dict