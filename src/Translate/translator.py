import argostranslate.translate
from src.configuration import Translate


class Translator:
    def __init__(self, config_vars: Translate):
        self.config_vars = config_vars
        self.from_lang = self.config_vars.from_lang
        self.to_lang = self.config_vars.to_lang

    def translate(self, text):
        return argostranslate.translate.translate(text, self.from_lang, self.to_lang)
