from src.utils import BaseStage
from src import logger


class Pipeline:
    def __init__(self):
        self.stages: list[BaseStage] = []
        self.logger = logger

    def add_stage(self, stage):
        self.stages.append(stage)
        return self

    def run(self, data, **kwargs):
        for stage in self.stages:
            self.logger.debug('running stage %s' % stage)
            if stage.__class__.__name__ == 'LanguageDetector':
                data = stage.run(data, from_lang=kwargs.get('from_lang'))
            else:
                data = stage.run(data, **kwargs)
            self.logger.debug('Data: %s' % stage)
        return data
