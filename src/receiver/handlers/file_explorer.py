from src.configuration import iter_files
from src.receiver.handlers import AbstractDataReceiver


class FileExplorerReceiver(AbstractDataReceiver):
    def __init__(self, directory_location: str, encoding: str, read_type: str):
        self.directory_location = directory_location
        self.encoding = encoding
        self.read_type = read_type

    def receive_data(self):
        return iter_files(directory_location=self.directory_location, encoding=self.encoding)
