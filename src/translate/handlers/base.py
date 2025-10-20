from abc import ABC, abstractmethod


class AbstractTranslate(ABC):

    @abstractmethod
    def translate(self, encrypted_data):
        raise NotImplementedError
