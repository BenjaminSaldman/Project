from src.configuration import Configuration
import yaml


def open_config_file(config_path):
    config_file = open(config_path, 'r')
    return config_file


def get_configuration_from_config_file(config_file):
    config_vars = yaml.safe_load(config_file)
    config_file.close()
    return config_vars


def load_config(config_file_path: str):
    config_file = open_config_file(config_file_path)
    config_vars = get_configuration_from_config_file(config_file)
    config_object = Configuration.from_dict(config_vars)
    return config_object
