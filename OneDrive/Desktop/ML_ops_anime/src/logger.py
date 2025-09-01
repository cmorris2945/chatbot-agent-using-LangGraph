import logging
import os ## Store all logs in a driectory that why we impot this
from datetime import datetime   # need date and time of each log

LOGS_DIR = "logs"
os.makedirs(LOGS_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOGS_DIR, f"log_{datetime.now().strftime('%Y-%m-%d')}.log")

logging.basicConfig(

    filename= LOG_FILE,
    format='%(asctime)s - %(levelname)s- %(message)s',
    level = logging.INFO

)


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger