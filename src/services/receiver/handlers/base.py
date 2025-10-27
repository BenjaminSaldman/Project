from abc import ABC, abstractmethod


class AbstractDataReceiver(ABC):
    @abstractmethod
    def receive_data(self):
        raise NotImplementedError
