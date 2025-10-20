from src.configuration import get_class_by_name


def get_handler_configuration(handler_configuration: dict[str, any]) -> (dict, dict):
    handler_module = handler_configuration.get('module')
    handler_parameters = handler_configuration.get('parameters')
    return handler_module, handler_parameters


def get_handler(config_vars):
    handler_name = config_vars.chosen
    handler_configuration: dict[str, any] = config_vars.handlers.get(handler_name)

    handler_module, handler_parameters = get_handler_configuration(handler_configuration)

    handler_cls = get_class_by_name(path=handler_module.get('path'),
                                    class_name=handler_module.get('class_name'))
    return handler_cls(**handler_parameters)
