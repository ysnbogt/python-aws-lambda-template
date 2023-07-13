from logging import Filter, LogRecord

from settings import ANSI_ESCAPE_PATTERN


class ANSIEscapeFilter(Filter):
    def filter(self, record: LogRecord) -> bool:
        record.msg = ANSI_ESCAPE_PATTERN.sub("", record.msg)
        return True
