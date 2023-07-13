from logging import FileHandler, Logger, StreamHandler

from libs.filters import ANSIEscapeFilter
from libs.formatters import ColoredFormatter, FileFormatter
from settings import LOG_FORMAT


def set_handlers(logger: Logger, log_file_path: str = None) -> Logger:
    # stream handler
    stream_handler = StreamHandler()
    stream_handler.setFormatter(ColoredFormatter(LOG_FORMAT))
    logger.addHandler(stream_handler)

    # file handler
    if log_file_path is not None:
        file_handler = FileHandler(log_file_path)
        file_handler.setFormatter(FileFormatter(LOG_FORMAT))
        file_handler.addFilter(ANSIEscapeFilter())
        logger.addHandler(file_handler)

    return logger
