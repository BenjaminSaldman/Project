from src.utils import DecryptorConfig, get_handler, BaseStage


class Decryptor(BaseStage):
    def __init__(self, decryptor_config: DecryptorConfig):
        self.handler = get_handler(decryptor_config)

    def run(self, encrypted_data, **kwargs):
        return self.handler.decrypt(encrypted_data)
