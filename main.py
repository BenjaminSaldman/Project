from src.configuration import load_config
from src.Decrypt.decryptions import Aes
from src.Translate import Translator


def main():
    config_location = 'configuration/config.yml'
    config_object = load_config(config_location)
    print("check:", config_object.check)
    aes = Aes(config_object.decrypt)

    encrypted_bytes = b'\x12{\xe6\xd9\x93\x8c\xd8\x15\x93\xaa4n)\xc9\xa7v\xb9h\xe356s\xab\x80\xf5v:v\x07\x81\xc2\xe1[\xb3X\x0c\xc7A\xc3VZ\xca\xaa\xa26=(\x83'
    plaintext_decrypted = aes.decrypt(encrypted_bytes)
    print("Decrypted:", plaintext_decrypted)

    translator = Translator(config_object.translate)
    print(translator.translate(plaintext_decrypted))


if __name__ == '__main__':
    main()
