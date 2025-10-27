from langdetect import detect
from src.services.language_detector.handlers import AbstractLanguageDetector


class LangDetectDetector(AbstractLanguageDetector):
    def __init__(self, default: bool):
        self.default = default

    def detect(self, raw_data):
        return raw_data, detect(raw_data)
