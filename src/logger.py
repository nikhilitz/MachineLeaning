import logging
import os
from datetime import datetime

# f-string generates the current date and time in the format: mm_dd_yyyy_HH_MM_SS.log
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Join current working directory with logs folder and log filename
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Create the logs directory if it doesn't exist. `exist_ok=True` prevents errors if the directory already exists
os.makedirs(logs_path, exist_ok=True)

# Create the full path for the log file by joining the logs directory path with the log file name
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure logging settings: write to LOG_FILE_PATH with a custom log format and set the log level to INFO
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)s %(name)s - %(levelname)s - %(message)s",  # Log format with timestamp, line number, logger name, level, and message
    level=logging.INFO  # Set the logging level to INFO
)

# if __name__ == "__main__":
#     # Log an info message indicating that logging has started
#     logging.info("Logging started")
