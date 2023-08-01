import logging
import colorlog
    
def setup_logging():
    # Create a logger
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)

    # Create a handler for console output
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Define log message formats
    log_format = (
        '%(log_color)s%(levelname)-8s%(reset)s - '
        '%(log_color)s%(message)s%(reset)s'
    )

    # Create a Formatter using colorlog.ColoredFormatter
    formatter = colorlog.ColoredFormatter(
        log_format,
        reset=True,
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'bold_red'
        }
    )

    # Set the Formatter for the console handler
    console_handler.setFormatter(formatter)

    # Add the console handler to the logger
    logger.addHandler(console_handler)

    return logger


    # # Set up the logging configuration
    # logger = setup_logging()

    # # Test the logging
    # logger.debug("This is a debug message.")
    # logger.info("This is an info message.")
    # logger.warning("This is a warning message.")
    # logger.error("This is an error message.")
    # logger.critical("This is a critical message.")