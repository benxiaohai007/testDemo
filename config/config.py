# config/config.py
import yaml
from pathlib import Path

def load_config(config_path: str = 'config.yaml'):
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

class Config:
    def __init__(self, config_dict):
        self.__dict__.update(config_dict)

    def __str__(self):
        return str(self.__dict__)
config = Config(load_config())


if __name__ == '__main__':
    config = Config(load_config())
    print(config)
    print(type(config))
    print(config.environments.get('test'))