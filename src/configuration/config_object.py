from dataclasses import dataclass
import typing as t


@dataclass
class DecryptType:
    module: str
    class_name: str

    @classmethod
    def from_dict(cls: t.Type["DecryptType"], my_object: dict):
        return cls(
            module=my_object["module"],
            class_name=my_object["class_name"]
        )


@dataclass
class AesDecryptType:
    iv: bytes

    @classmethod
    def from_dict(cls: t.Type["AesDecryptType"], my_object: dict):
        return cls(
            iv=my_object["iv"]
        )


@dataclass
class Decrypt:
    decrypt_type: DecryptType
    key: bytes
    aes: AesDecryptType

    @classmethod
    def from_dict(cls: t.Type["Decrypt"], my_object: dict):
        decrypt_type = DecryptType.from_dict(my_object["decrypt_type"])
        aes = AesDecryptType.from_dict(my_object["aes"])
        return cls(
            decrypt_type=decrypt_type,
            key=my_object["key"],
            aes=aes,
        )


@dataclass
class Translate:
    from_lang: str
    to_lang: str

    @classmethod
    def from_dict(cls: t.Type["Translate"], my_object: dict):
        return cls(
            from_lang=my_object["from_lang"],
            to_lang=my_object["to_lang"]
        )


@dataclass
class Configuration:
    check: int
    decrypt: Decrypt
    translate: Translate

    @classmethod
    def from_dict(cls: t.Type["Configuration"], my_object: dict):
        decrypt = Decrypt.from_dict(my_object["decrypt"])
        translate = Translate.from_dict(my_object["translate"])
        return cls(
            check=my_object["check"],
            decrypt=decrypt,
            translate=translate

        )
