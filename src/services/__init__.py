from .decrypt.decryptor import Decryptor
from .language_detector import LanguageDetector
from .receiver import DataReceiver
from .translate import Translator
from ..developer_config import config_object

decryptor = Decryptor(config_object.decryptor)
data_receiver = DataReceiver(config_object.data_receiver)
translator = Translator(config_object.translator)
language_detector = LanguageDetector(config_object.language_detector)
