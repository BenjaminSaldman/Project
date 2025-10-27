from src.utils import DataReceiverConfig
from src.utils import get_handler


class DataReceiver:
    def __init__(self, data_receiver_config: DataReceiverConfig):
        self.handler = get_handler(data_receiver_config)

    def receive_data(self):
        return self.handler.receive_data()
