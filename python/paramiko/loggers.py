"""
Logging module in python used to log the data to a file 
these log files are used to analyze the testcase results 

these are different logging levels
1)critical
2) Info
3) error
4) warning
5) debug

"""
import logging
import os
import time
from datetime import datetime

name = "Pranai"
logger = logging.getLogger("My_logger")
logger.setLevel(logging.DEBUG)  # Set the logging level

# Correct the time format using datetime
file_format = f"Project_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

# Create a file handler to write logs to a file
file_handler = logging.FileHandler(file_format)  # Use the correct file name
file_handler.setLevel(logging.DEBUG)

# Create a console handler to output logs to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)  # Only log errors to the console

# Create a formatter and set it for both handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Example log messages
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")

# Get the hostname of the current system and log it
hostname = os.popen("hostname").read().strip()
logger.info(f"Hostname of the current system is {hostname}")
