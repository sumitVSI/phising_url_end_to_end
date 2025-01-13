import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format = '[%(asctime)s] : %(message)s:')

while True:
    project_name = input("Enter the project name :")
    if project_name != '':
        break

project_files_list = [

    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",

    "config/config.yaml",
    "config/params.yaml",
    "config/schema.yaml",

    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research"

]

for folder_and_file_paths in project_files_list:

    folder_and_file_paths = Path(folder_and_file_paths)

    folder_name,file_name = os.path.split(folder_and_file_paths)

    if folder_name != "":

        os.makedirs(folder_name,exist_ok=True)

        logging.info(f"Foder created for : {folder_name} for filename : {file_name}")

    if (not os.path.exists(folder_and_file_paths)) or (os.path.getsize(folder_and_file_paths)==0):

        with open(folder_and_file_paths,"w") as file:
            pass
        logging.info(f"Emprty file created : {folder_and_file_paths}")

    else:
        logging.info(f"File already exist : {folder_and_file_paths}")