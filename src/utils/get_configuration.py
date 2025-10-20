def get_handler_configuration(decryptor_handler_configuration: dict[str, any]) -> (dict, dict):
    handler_module = decryptor_handler_configuration.get('module')
    handler_parameters = decryptor_handler_configuration.get('parameters')
    return handler_module, handler_parameters
