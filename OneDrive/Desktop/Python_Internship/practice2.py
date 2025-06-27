import logging
logger = logging.getLogger(__name__)

stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('Log_file.log')
stream_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.ERROR)

handler_format = logging.Formatter('%(asctime)s - %(name)s -  %(levelname)s - %(message)s')
stream_handler.setFormatter(handler_format)
file_handler.setFormatter(handler_format)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.error("Something is having error")
logger.debug("Just a debug")
