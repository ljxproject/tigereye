from datetime import datetime


DEFAULT_DATETIME_FORMAT = '%Y%m%d%H%M%S'
SIMPLE_DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'


def now():
    return datetime.now().strftime(DEFAULT_DATETIME_FORMAT)