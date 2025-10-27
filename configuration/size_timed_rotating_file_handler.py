import os
from logging.handlers import TimedRotatingFileHandler


class SizeTimedRotatingFileHandler(TimedRotatingFileHandler):
    def __init__(self, filename, when='midnight', interval=1, backupCount=7,
                 maxBytes=10 * 1024 * 1024, encoding=None, delay=False):
        super().__init__(filename, when=when, interval=interval,
                         backupCount=backupCount, encoding=encoding,
                         delay=delay)
        self.maxBytes = maxBytes

    def shouldRollover(self, record):
        if self.maxBytes > 0:
            if os.path.exists(self.baseFilename):
                if os.path.getsize(self.baseFilename) >= self.maxBytes:
                    return True  # Size based rollover

        # Time-based rollover
        return super().shouldRollover(record)

    def doRollover(self):
        # Rotate by size first
        if os.path.getsize(self.baseFilename) >= self.maxBytes:
            self._rotate_by_size()

        # Then rotate by time
        super().doRollover()

    def _rotate_by_size(self):
        if self.maxBytes <= 0:
            return

        if os.path.exists(self.baseFilename) and os.path.getsize(self.baseFilename) >= self.maxBytes:
            # Determine the new filename
            for i in range(self.backupCount - 1, 0, -1):
                sfn = f"{self.baseFilename}.{i}"
                dfn = f"{self.baseFilename}.{i + 1}"
                if os.path.exists(sfn):
                    os.rename(sfn, dfn)
            dfn = self.baseFilename + ".1"
            if os.path.exists(self.baseFilename):
                os.rename(self.baseFilename, dfn)
