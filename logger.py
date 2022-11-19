import logging

_log_format = f"%(asctime)s [%(levelname)s] %(message)s"

def get_file_handler():
    file_handler = logging.FileHandler("api.log")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(_log_format))
    return file_handler


def get_logger(name):
    logger = logging.FileHandler(name)
    logger.setLevel(logging.DEBUG)
    logger.setFormatter(logging.Formatter(_log_format))
    return logger