from decouple import config
from enum import Enum

class LoggingRenderer(str, Enum):
    JSON = "json"
    CONSOLE = "console"

def get_logging_config():
    return {
        'level': config('LOGGING_LEVEL', default='INFO'),
        'format': config('LOGGING_FORMAT', default='%Y-%m-%d %H:%M:%S'),
        'is_utc': config('LOGGING_IS_UTC', default=False, cast=bool),
        'renderer': LoggingRenderer(config('LOGGING_RENDERER', default='json')),
        'log_unhandled': config('LOGGING_UNHANDLED', default=False, cast=bool)
    }
