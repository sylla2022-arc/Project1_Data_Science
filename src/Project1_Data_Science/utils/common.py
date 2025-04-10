import sys
from pathlib import Path

# Ajoute le répertoire parent au PATH Python
sys.path.append(str(Path(__file__).parent.parent))

import os
import yaml
from src.Project1_Data_Science import logger    
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox :
    """Read yaml file and return a ConfigBox object
    Value Error if ymal file is empty"""
    print(f"Lecture de YAML depuis {path_to_yaml}")
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            config = yaml.safe_load(yaml_file)
            return ConfigBox(config)
    except BoxValueError as e:
        raise ValueError(f"Error reading the yaml file: {e}")
    except Exception as e:
        logger.error(f"Error reading the yaml file: {e}")
        raise e 

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")

@ensure_annotations
def load_json(path:Path) -> ConfigBox:
    """Save data to a pickle file"""
    with open(path) as file:
        content = json.load(file)
        
    logger.info(f"json file loaded succesfully to {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data:dict, path:Path) -> None:
    """Save data to a pickle file"""
    joblib.dump(value=data, filename=path)
    logger.info(f"Binaty file saved to {path}")

@ensure_annotations
def load_bin(path:Path) -> Any:
    """Save data to a pickle file"""
    data = joblib.load(path)
    logger.info(f"Binary file loaded succesfully to {path}")
    return data
