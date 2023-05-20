import logging
import os
from datetime import datetime

# Creating logs directory to store log in files
LOG_DIR = "logs"
logs_path = os.path.join(os.getcwd(), LOG_DIR)

# Creating logs_path if it does not exists.
os.makedirs(logs_path, exist_ok=True)

# Creating file name for log file based on current timestamp
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
log_file_name = f"log_{CURRENT_TIME_STAMP}.log"

# Creating file path for projects.
log_file_path = os.path.join(logs_path, log_file_name)


logging.basicConfig(
    filename=log_file_path,
    filemode="w",
    format="[%(asctime)s] %(levelname)s:  %(lineno)d %(name)s - %(funcName)s : %(message)s",
    level=logging.INFO,
)
