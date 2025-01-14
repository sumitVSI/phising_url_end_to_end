import os
import yaml
import json
import joblib
import pandas as pd
import numpy as np
from box import ConfigBox
from box.exceptions import BoxValueError
from pathlib import Path
from typing import Any
from ensure import ensure_annotations

from phising_project.logging import logger



@ensure_annotations
def read_yaml_file(yaml_filepath:Path) -> ConfigBox:
    """reads yaml file content and returns the content in ConfigBox type

    Args:
        yaml_filepath (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: error
    
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(yaml_filepath) as file:
            file_content = yaml.safe_load(file)
            logger.info(f"yaml file : {yaml_filepath} content loaded successfully")
            return ConfigBox(file_content)
    except BoxValueError:
        raise ValueError(f"yaml file : {yaml_filepath} has no content")
    except Exception as e:
        raise e
        
@ensure_annotations
def create_directories(directory_path: list,verbose=True):
    """creating list of directories

    Args:
        directory_path (list): list of directory paths
    """
    for path in directory_path:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"directory created at : {path}")

@ensure_annotations
def save_json(path:Path,data:dict):
    """saving json data

    Args:
        path (Path): json file path
        data (dict): data to besaved in json file
    """

    with open(path,"w") as f:
        json.dump(data,f,indent=4)

    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path:Path) -> ConfigBox:
    """loading json file data

    Args:
        path (Path): json file path

    Returns:
        ConfigBox: configbox type(data as class attributes)
    """

    with open(path) as f:
        file_content = json.load(f)

    logger.info(f"json file loaded successfully from:{Path}")

    return ConfigBox(file_content)



@ensure_annotations
def save_bin(data: Any, path:Path):
    """saving binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to the saved binary file
    """

    joblib.dump(data,filename=path)
    logger.info(f"binary file saved at: {path}")



def load_bin(path: Path) -> Any:
    """loading binary data froma path

    Args:
        Path (Path): path to the binary file

    Returns:
        Any: object stored in the file
    """

    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")

    return data

@ensure_annotations
def get_size(path:Path) -> str:
    """get size of a file in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

