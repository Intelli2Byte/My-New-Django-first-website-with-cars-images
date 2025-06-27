import logging
import logging.config

logging.config.fileConfig('logfile.conf')
logger = logging.getLogger('easyLogger')
logger.debug('This is a debug log')