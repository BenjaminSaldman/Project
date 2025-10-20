import importlib


def get_class_by_name(path: str, class_name: str):
    module = importlib.import_module(path)
    return getattr(module, class_name)
