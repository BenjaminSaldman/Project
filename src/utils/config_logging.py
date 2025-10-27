import json
import logging.config


def config_logging(configuration_path):
    with open(configuration_path, 'r') as file:
        config = json.load(file)
        logging.config.dictConfig(config)


def setup_logging(configuration_path: str) -> None:
    config_logging(configuration_path)
    logging.getLogger('debug_logger').debug('Logging configured')
