from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
from src.decrypt.handlers import AbstractDecrypt


class AesDecryptor(AbstractDecrypt):
    def __init__(self, key, iv, encode):
        self.key = base64.b64decode(key)
        self.iv = base64.b64decode(iv)
        self.encode = encode

    def decrypt(self, encrypted_data) -> str:
        cipher = Cipher(
            algorithms.AES(self.key),
            modes.CBC(self.iv),
            backend=default_backend()
        )
        decryptor = cipher.decryptor()

        decrypted_padded = decryptor.update(encrypted_data) + decryptor.finalize()

        padding_len = decrypted_padded[-1]
        decrypted = decrypted_padded[:-padding_len]

        return decrypted.decode(self.encode)
