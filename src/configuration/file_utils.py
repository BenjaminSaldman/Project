import os

import yaml

from src.configuration import Configuration

BINARY_EXTENSIONS = {".bin", ".dat", ".exe", ".zip", ".png", ".jpg", ".jpeg", ".pdf"}


def load_config(config_location: str) -> Configuration:
    with open(config_location, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    return Configuration(**data)


def iter_file(full_path: str, encoding: str = None, read_type: str = "r"):
    with open(full_path, read_type, encoding=encoding) as file:
        yield file.read()


def is_binary_file(file_name: str) -> bool:
    _, ext = os.path.splitext(file_name)
    return ext.lower() in BINARY_EXTENSIONS


def get_file_read_params(file_name: str, default_encoding: str = "utf-8") -> tuple[str, str | None]:
    if is_binary_file(file_name):
        return "rb", None  # binary file
    return "r", default_encoding  # text file


def find_files_in_directory(directory_location: str):
    for file_name in os.listdir(directory_location):
        full_file_path = os.path.join(directory_location, file_name)
        if os.path.isfile(full_file_path):
            yield full_file_path


def iter_files(directory_location: str, encoding: str = "utf-8"):
    for full_file_path in find_files_in_directory(directory_location):
        file_name = os.path.basename(full_file_path)
        read_type, file_encoding = get_file_read_params(file_name, encoding)
        yield from iter_file(full_path=full_file_path, encoding=file_encoding, read_type=read_type)
