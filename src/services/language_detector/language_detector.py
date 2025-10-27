from src.utils import LanguageDetectorConfig, get_handler, BaseStage


class LanguageDetector(BaseStage):
    def __init__(self, language_detector_config: LanguageDetectorConfig):
        self.handler = get_handler(language_detector_config)

    def run(self, raw_data, **kwargs):
        return self.handler.detect(raw_data)
