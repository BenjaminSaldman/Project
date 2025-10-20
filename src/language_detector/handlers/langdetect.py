from langdetect import detect
from src.language_detector.handlers import AbstractLanguageDetector


class LangDetectDetector(AbstractLanguageDetector):
    def __init__(self, default: bool):
        self.default = default

    def detect(self, raw_data) -> str:
        return detect(raw_data)
