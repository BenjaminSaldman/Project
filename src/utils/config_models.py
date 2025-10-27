from typing import Any, Dict

from pydantic import BaseModel


class DecryptorConfig(BaseModel):
    chosen: str
    handlers: Dict[str, Any]


class TranslatorConfig(BaseModel):
    chosen: str
    handlers: Dict[str, Any]


class LanguageDetectorConfig(BaseModel):
    chosen: str
    handlers: Dict[str, Any]


class DataReceiverConfig(BaseModel):
    chosen: str
    handlers: Dict[str, Any]


class Configuration(BaseModel):
    decryptor: DecryptorConfig
    translator: TranslatorConfig
    language_detector: LanguageDetectorConfig
    data_receiver: DataReceiverConfig
