import os
import logging
import logging.config


CONFIG_DIR = os.path.abspath("../config/logger.conf")
logging.config.fileConfig(CONFIG_DIR)
logger = logging.getLogger(__name__)
