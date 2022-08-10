import logging
from logging.handlers import RotatingFileHandler


class Logger(logging.getLoggerClass()):
    log_filename = "logfile"
    log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    log_level = logging.DEBUG
    log_byte_size = 200 * 1024

    def __init__(self):
        self.root = logging.getLogger()
        handler = self._setup_handler()
        self.root.addHandler(handler)

    def info(self, log: str):
        self.root.info(log)

    def error(self, log: str, err: Exception):
        self.root.error(f"{log} \n{err}")

    def _setup_handler(self):
        handler = RotatingFileHandler(self.log_filename, encoding="utf-8", maxBytes=self.log_byte_size, backupCount=1)
        handler.setFormatter(self.log_format)
        handler.setLevel(self.log_level)
        return handler
