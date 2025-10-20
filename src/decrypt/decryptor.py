from src.configuration import get_class_by_name
from src.configuration import DecryptorConfig
from src.utils import get_handler_configuration


class Decryptor:
    def __init__(self, decryptor_config: DecryptorConfig):
        handler_name = decryptor_config.chosen
        decryptor_handler_configuration: dict[str, any] = decryptor_config.handlers.get(handler_name)

        handler_module, handler_parameters = get_handler_configuration(decryptor_handler_configuration)

        self.handler_cls = get_class_by_name(path=handler_module.get('path'),
                                             class_name=handler_module.get('class_name'))
        self.handler = self.handler_cls(**handler_parameters)

    def decrypt(self, encrypted_data):
        return self.handler.decrypt(encrypted_data)
