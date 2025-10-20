import argostranslate.translate
from src.translate.handlers import AbstractTranslate


class Argostranslate(AbstractTranslate):
    def __init__(self, from_lang, to_lang):
        self.from_lang = from_lang
        self.to_lang = to_lang

    def translate(self, text):
        return argostranslate.translate.translate(text, self.from_lang, self.to_lang)
