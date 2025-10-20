from src.Decrypt import Decryptor
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
from src.configuration import Decrypt


class Aes(Decryptor):
    def __init__(self, decrypt_config_vars: Decrypt):
        aes_config_vars = decrypt_config_vars.aes
        super().__init__(base64.b64decode(decrypt_config_vars.key))
        self.iv = base64.b64decode(aes_config_vars.iv)

    def decrypt(self, encrypted_data) -> str:
        cipher = Cipher(
            algorithms.AES(self.decryption_key),
            modes.CBC(self.iv),
            backend=default_backend()
        )
        decryptor = cipher.decryptor()

        decrypted_padded = decryptor.update(encrypted_data) + decryptor.finalize()

        padding_len = decrypted_padded[-1]
        decrypted = decrypted_padded[:-padding_len]

        return decrypted.decode("utf-8")
