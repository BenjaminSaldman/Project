from src.configuration import get_class_by_name
from src.configuration import TranslatorConfig
from src.utils import get_handler_configuration


class Translator:
    def __init__(self, translator_config: TranslatorConfig):
        handler_name = translator_config.chosen
        translator_handler_configuration: dict[str, any] = translator_config.handlers.get(handler_name)

        handler_module, handler_parameters = get_handler_configuration(translator_handler_configuration)

        self.handler_cls = get_class_by_name(path=handler_module.get('path'),
                                             class_name=handler_module.get('class_name'))
        self.handler = self.handler_cls(**handler_parameters)

    def translate(self, text):
        return self.handler.translate(text)
