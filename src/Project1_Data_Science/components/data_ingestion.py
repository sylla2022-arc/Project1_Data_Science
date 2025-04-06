import os
import requests
import urllib.request  as request
from src.Project1_Data_Science import logger
import zipfile
from src.Project1_Data_Science.constants import *
from src.Project1_Data_Science.entity.config_entity import (DataIngestionconfig)

## Component data Ingestion

class DataIngestion:
    def __init__(self, config: DataIngestionconfig):
        self.config = config
    # downloading the zip file from the source URL
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            try:
                filename, header =request.urlretrieve(
                    self.config.source_URL, 
                    self.config.local_data_file)
                logger.info(f"{filename} downloaded: \n  {header}")
            except Exception as e:
                raise Exception(f"Error downloading {filename}: {e}")
        else :
            logger.info(f"File already exists: {self.config.local_data_file}")
    # extracting the zip file
    def extract_zip_file(self):
        """Extracts the zip file to the specified directory.
        If the directory does not exist, it will be created.
        function return none
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info(f"Extracted files to {unzip_path}")     