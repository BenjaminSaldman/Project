from src.configuration import DecryptorConfig
from src.utils import get_handler


class Decryptor:
    def __init__(self, decryptor_config: DecryptorConfig):
        self.handler = get_handler(decryptor_config)

    def decrypt(self, encrypted_data):
        return self.handler.decrypt(encrypted_data)
