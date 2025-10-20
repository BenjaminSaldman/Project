from pydantic import BaseModel
from typing import Any, Dict


class DecryptorConfig(BaseModel):
    chosen: str
    handlers: Dict[str, Any]


class TranslatorConfig(BaseModel):
    chosen: str
    handlers: Dict[str, Any]


class Configuration(BaseModel):
    decryptor: DecryptorConfig
    translator: TranslatorConfig
