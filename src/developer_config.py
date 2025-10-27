import logging
import os

from src.utils import Configuration, load_config, setup_logging

config_object: Configuration = load_config(os.getenv('CONF_FILE_LOCATION'))
setup_logging(os.getenv('LOGS_CONF_FILE_LOCATION'))
logger = logging.getLogger(os.getenv('ENV'))
