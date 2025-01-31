# config/config.py
import yaml
from pathlib import Path

def load_config(config_path: str = 'config/config.yaml'):
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

class Config:
    def __init__(self, config_dict):
        self.__dict__.update(config_dict)

config = Config(load_config())
