from abc import ABC, abstractmethod


class AbstractDecrypt(ABC):

    @abstractmethod
    def decrypt(self, encrypted_data):
        raise NotImplementedError
