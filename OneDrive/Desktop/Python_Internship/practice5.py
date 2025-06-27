
import logging
import traceback

try:
    numbers = [10, 20, 30, 40, 50, 60]
    chosen_number = numbers[10]
except:
    logging.error("Error: %s", traceback.format_exc())