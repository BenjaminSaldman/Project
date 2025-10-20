from src.configuration import Configuration
import yaml


def load_config(config_location: str) -> Configuration:
    with open(config_location, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    return Configuration(**data)
