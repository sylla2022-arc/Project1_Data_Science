import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


project_name = 'Project1_Data_Science'

list_of_files = [".github/workflows/.gitkeep",
 f"src/{project_name}/__init__.py",
 f"src/{project_name}/utils.py",
 f"src/{project_name}/components/__init__.py",
  f"src/{project_name}/utils/__init__.py",
  f"src/{project_name}/utils/common.py",
 f"src/{project_name}/config/__init__.py",
f"src/{project_name}/config/configuration.py",
f"src/{project_name}/pipeline/__init__.py",
f"src/{project_name}/entity/__init__.py",
f"src/{project_name}/entity/config_entity.py",
f"src/{project_name}/constants/__init__.py",
"config/config.yml",
"params.yaml",
"schema.yaml",
"main.py",
"Dockerfile",
"setup.py",
"research/research.ipynb",
"templates/index.html",
"app.py",
 ]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")
    
    
    if (not os.path.exists(filepath) or (os.path.getsize(filepath)==0)):
        with open(filepath, 'w') as file:
            file.write("")
            logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info(f"File {filename} already exists: {filepath}")