import sys
from wasteDetection.logger import logging
from wasteDetection.exception import AppException

logging.info("This is to check custom log.")


try:
    a = 3/ "3"
except Exception as e:
    raise AppException(e, sys)