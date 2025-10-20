from src.configuration import TranslatorConfig
from src.utils import get_handler


class Translator:
    def __init__(self, translator_config: TranslatorConfig):
        self.handler = get_handler(translator_config)

    def translate(self, text, from_lang):
        return self.handler.translate(text, from_lang)
