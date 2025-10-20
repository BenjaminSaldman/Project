from typing import Type
from src.configuration import get_class_by_name, Decrypt
from src.Decrypt import Decryptor


def initialize_decryption(decrypt_config_object: Decrypt) -> Decryptor:
    decryption_class: Type[Decryptor] = get_class_by_name(decrypt_config_object.decrypt_type.module,
                                                          decrypt_config_object.decrypt_type.class_name)
    decryption: Decryptor = decryption_class(decrypt_config_object)

    return decryption

