from abc import ABC, abstractmethod


class Decryptor(ABC):
    def __init__(self, decryption_key):
        self.decryption_key = decryption_key

    @abstractmethod
    def decrypt(self, encrypted_data):
        raise NotImplementedError
