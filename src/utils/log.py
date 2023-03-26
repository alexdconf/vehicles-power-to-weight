import os
import logging
import logging.config


class Logger:
    log = None
    
    @classmethod
    def initialize(cls, config_dir):
        logging.config.fileConfig(config_dir)
        logger = logging.getLogger(__name__)
        cls.log = logger
