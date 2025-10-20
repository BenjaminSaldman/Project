import warnings

warnings.filterwarnings(
    "ignore",
    message="pkg_resources is deprecated",
    category=UserWarning
)
import argostranslate.translate
from src.translate.handlers import AbstractTranslate


class Argostranslate(AbstractTranslate):
    def __init__(self, from_lang, to_lang):
        self.from_lang = from_lang
        self.to_lang = to_lang

    def translate(self, text, from_lang=None):
        if from_lang is None:
            from_lang = self.from_lang
        return argostranslate.translate.translate(text, from_lang, self.to_lang)
