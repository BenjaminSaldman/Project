from src.utils import BaseStage
# from src import logger
import logging
import os


class Pipeline:
    def __init__(self):
        self.stages: list[BaseStage] = []
        logger = logging.getLogger(os.getenv('ENV'))
        self.logger = logger

    def add_stage(self, stage):
        self.stages.append(stage)
        return self

    def run(self, data, **kwargs):
        for stage in self.stages:
            self.logger.debug('running stage %s' % stage)
            if stage.__class__.__name__ == 'LanguageDetector':
                data = stage.run(data)
            elif stage.__class__.__name__ == 'Translator':
                text, lang_from = data
                data = stage.run(text, from_lang=lang_from)
            else:
                data = stage.run(data, **kwargs)
            if isinstance(data, str):
                self.logger.debug('Data: %s' % data)
        return data
