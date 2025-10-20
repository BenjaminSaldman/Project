from abc import ABC, abstractmethod


class AbstractLanguageDetector(ABC):

    @abstractmethod
    def detect(self, raw_data: str):
        raise NotImplementedError
