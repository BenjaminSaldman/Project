from src.translate import Translator
from src.decrypt import Decryptor
from src.language_detector import LanguageDetector
from src.configuration import Configuration, load_config


def main():
    config_location = 'configuration/config.yml'
    config_object: Configuration = load_config(config_location)

    decryptor = Decryptor(config_object.decryptor)

    encrypted_bytes = b'\x12{\xe6\xd9\x93\x8c\xd8\x15\x93\xaa4n)\xc9\xa7v\xb9h\xe356s\xab\x80\xf5v:v\x07\x81\xc2\xe1[\xb3X\x0c\xc7A\xc3VZ\xca\xaa\xa26=(\x83'
    plaintext = decryptor.decrypt(encrypted_bytes)
    print("Decrypted:", plaintext)

    language_detector = LanguageDetector(config_object.language_detector)

    translator = Translator(config_object.translator)
    print(translator.translate(plaintext, language_detector.detect(plaintext[:50])))


if __name__ == '__main__':
    main()
