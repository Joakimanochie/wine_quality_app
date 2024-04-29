import os
from pathlib import Path
import logging

#logging structure
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "winequality"


#list of file to create
list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.py",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"


]


for filepath in list_of_files:
    filepath = Path(filepath)

    # Spliting file name and directory
    filedir, filename = os.path.split(filepath)

    # checks if directory name is not empty then creates it
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")
    
    # checking if file exists in the path and checks the file size, then creates it
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info(f"{filename} already exists")