import yaml
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import sys, os
import numpy as np
import dill
import pickle


def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, 'rb') as  yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise NetworkSecurityException(e, sys)


def write_yaml_file(fiel_path: str, content: object, replace: bool=False) -> None:
    try:
        if replace:
            if os.path.exists(fiel_path):
                os.remove(fiel_path)
        os.makedirs(os.path.dirname(fiel_path), exist_ok=True)
        with open(fiel_path, "w") as file:
            yaml.dump(content, file)
    except Exception as e:
        raise NetworkSecurityException(e, sys)