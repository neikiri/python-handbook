"""
Logging Example - Logging Messages

This example demonstrates:
- Basic logging configuration
- Different log levels
- Logging to files
- Logging with format strings
- Logger instances
"""

import logging
import sys

print("=== Basic Logging ===")

# Configure basic logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s"
)

# Log messages at different levels
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
print()

print("=== Log Levels ===")

# Log levels (in order of severity):
# DEBUG - Detailed information for debugging
# INFO - General information
# WARNING - Something unexpected happened
# ERROR - A more serious problem
# CRITICAL - A very serious error

# Default level is WARNING, so only WARNING, ERROR, CRITICAL are shown by default
logging.basicConfig(level=logging.WARNING)
print("With level=WARNING:")
logging.debug("Debug message (won't show)")
logging.info("Info message (won't show)")
logging.warning("Warning message (will show)")
logging.error("Error message (will show)")
logging.critical("Critical message (will show)")
print()

print("=== Logging to a File ===")

# Configure logging to file
logging.basicConfig(
    filename="example.log",
    filemode="w",  # "w" for overwrite, "a" for append
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.debug("This will be written to example.log")
logging.info("This too")
logging.warning("And this")

print("Logged messages to example.log")
print()

# Read and show the log file
with open("example.log", "r") as f:
    print("Content of example.log:")
    print(f.read())
print()

print("=== Custom Log Format ===")

# Format with more details
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logging.info("Message with timestamp and logger name")
print()

print("=== Logger Instances ===")

# Create a named logger
logger = logging.getLogger("myapp")

# Configure handler for this logger
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

# Use the logger
logger.debug("Debug message from myapp")
logger.info("Info message from myapp")
logger.warning("Warning message from myapp")
print()

print("=== Logging with Variables ===")

name = "Alice"
age = 30
city = "New York"

# Using f-strings (Python 3.6+)
logging.info(f"User: {name}, Age: {age}, City: {city}")

# Using format string
logging.info("User: {}, Age: {}, City: {}".format(name, age, city))

# Using % formatting (older style)
logging.info("User: %s, Age: %d, City: %s", name, age, city)
print()

print("=== Exception Logging ===")

# Log exceptions with traceback
try:
    result = 10 / 0
except ZeroDivisionError as e:
    logging.error("Division failed: %s", e, exc_info=True)
print()

print("=== Practical Example: Application Logger ===")

# Create a logger for your application
app_logger = logging.getLogger("myapp")
app_logger.setLevel(logging.DEBUG)

# Console handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter("%(levelname)s: %(message)s")
console_handler.setFormatter(console_formatter)

# File handler
file_handler = logging.FileHandler("app.log", mode="w")
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

# Add handlers to logger
app_logger.addHandler(console_handler)
app_logger.addHandler(file_handler)

# Use the logger
app_logger.info("Application started")
app_logger.debug("Loading configuration...")
app_logger.info("Configuration loaded")
app_logger.warning("Using default configuration")

try:
    # Simulate an error
    raise ValueError("Something went wrong!")
except ValueError as e:
    app_logger.error("An error occurred: %s", e, exc_info=True)

app_logger.info("Application finished")

print("Logged to both console and app.log")
print()

print("=== Logging Configuration ===")

# Better approach: use dictConfig for complex configurations
import logging.config

logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "standard",
            "stream": "ext://sys.stdout",
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "standard",
            "filename": "config_app.log",
            "mode": "w",
        },
    },
    "loggers": {
        "myapp": {
            "level": "DEBUG",
            "handlers": ["console", "file"],
            "propagate": False,
        },
    },
}

logging.config.dictConfig(logging_config)
logger = logging.getLogger("myapp")

logger.info("Using dictConfig for logging")
logger.debug("Debug message with config")

print("Logged using dictConfig to config_app.log")
print()

print("=== Best Practices ===")

print("1. Use logging instead of print() for debugging")
print("2. Use appropriate log levels")
print("3. Use logger instances for different modules")
print("4. Configure logging at the start of your application")
print("5. Use exc_info=True when logging exceptions")
print("6. Don't log sensitive information (passwords, keys)")
print("7. Use file logging for production applications")
print("8. Consider log rotation for long-running applications")
