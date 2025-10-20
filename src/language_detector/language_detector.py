from src.configuration import LanguageDetectorConfig
from src.utils import get_handler


class LanguageDetector:
    def __init__(self, language_detector_config: LanguageDetectorConfig):
        self.handler = get_handler(language_detector_config)

    def detect(self, raw_data):
        return self.handler.detect(raw_data)
