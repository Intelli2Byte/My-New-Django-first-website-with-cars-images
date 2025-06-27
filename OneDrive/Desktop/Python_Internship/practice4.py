import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s -  %(levelname)s - %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S')

logging.debug("This is a debug log")
logging.info("This is an info log")
logging.warning("This is a warning log")
logging.error("This is an error log")
logging.critical("This is a critical log")