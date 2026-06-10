import logging
import os


def get_logger(name: str) -> logging.Logger:
    """
    Returns a logger that writes to both console and logs/logs.log
    at the project root.

    Usage:
        from utils.loggerCreator import get_logger
        logger = get_logger(__name__)
    """

    # logs/ folder sits at the project root (two levels up from utils/)
    log_dir  = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "logs.log")

    logger = logging.getLogger(name)

    # Guard: don't add duplicate handlers on re-import
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        fmt="%(asctime)s  %(levelname)-8s  %(name)s  %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    
    file_handler = logging.FileHandler(log_file, mode="a", encoding="utf-8")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger