from src.configuration import Configuration, load_config
from src.decrypt import Decryptor
from src.language_detector import LanguageDetector
from src.receiver import DataReceiver
from src.translate import Translator
import logging.config
from src.configuration import setup_logging


def main():
    config_location = 'configuration/config.yml'
    config_object: Configuration = load_config(config_location)

    setup_logging('configuration/logs.json')

    debug_logger = logging.getLogger('debug_logger')

    decryptor = Decryptor(config_object.decryptor)

    data_receiver = DataReceiver(config_object.data_receiver)
    data_receiver_iterator = data_receiver.receive_data()

    for encrypted_file_content in data_receiver_iterator:
        plaintext = decryptor.decrypt(encrypted_file_content)
        debug_logger.debug("Decrypted data: %s" % plaintext)

        language_detector = LanguageDetector(config_object.language_detector)

        translator = Translator(config_object.translator)
        translated_data = translator.translate(plaintext, language_detector.detect(plaintext[:50]))
        debug_logger.debug(f"Translated data: %s" % translated_data)


if __name__ == '__main__':
    main()
