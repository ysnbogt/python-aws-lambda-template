from __future__ import annotations

from logging import DEBUG, ERROR, INFO, WARNING, Formatter, LogRecord

from termcolor import colored

from settings import ANSI_ESCAPE_PATTERN


class ColoredFormatter(Formatter):
    def format(self, record: LogRecord) -> str:
        levelname = ""
        if record.levelno == INFO:
            levelname = colored(record.levelname, "green")
        elif record.levelno == WARNING:
            levelname = colored(record.levelname, "yellow")
        elif record.levelno == ERROR:
            levelname = colored(record.levelname, "red")
        elif record.levelno == DEBUG:
            levelname = colored(record.levelname, "cyan")
        else:
            levelname = record.levelname
        record.levelname = levelname
        return super().format(record)


class FileFormatter(Formatter):
    def format(self, record: LogRecord) -> str:
        msg = super().format(record)
        return ANSI_ESCAPE_PATTERN.sub("", msg)
