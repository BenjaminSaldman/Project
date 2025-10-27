from src.configuration import Configuration, load_config
from src.decrypt import Decryptor
from src.language_detector import LanguageDetector
from src.receiver import DataReceiver
from src.translate import Translator


def main():
    config_location = 'configuration/config.yml'
    config_object: Configuration = load_config(config_location)

    decryptor = Decryptor(config_object.decryptor)

    data_receiver = DataReceiver(config_object.data_receiver)
    data_receiver_iterator = data_receiver.receive_data()

    for encrypted_file_content in data_receiver_iterator:
        plaintext = decryptor.decrypt(encrypted_file_content)
        print("Decrypted:", plaintext)

        language_detector = LanguageDetector(config_object.language_detector)

        translator = Translator(config_object.translator)
        print(translator.translate(plaintext, language_detector.detect(plaintext[:50])))
        print('*************************')


if __name__ == '__main__':
    main()
