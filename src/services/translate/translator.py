from src.utils import TranslatorConfig, get_handler, BaseStage


class Translator(BaseStage):
    def __init__(self, translator_config: TranslatorConfig):
        self.handler = get_handler(translator_config)

    def run(self, text, **kwargs):
        return self.handler.translate(text, kwargs.get('from_lang'))
