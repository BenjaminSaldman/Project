from dataclasses import dataclass
import typing as t


@dataclass
class Decrypt:
    key: bytes
    iv: bytes

    @classmethod
    def from_dict(cls: t.Type["Decrypt"], my_object: dict):
        return cls(
            key=my_object["key"],
            iv=my_object["iv"]
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
