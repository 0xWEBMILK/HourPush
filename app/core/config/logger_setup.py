
# src/logger_setup.py
import logging
import sys
import json
from .config_setup import log_settings

# JSON логгер
class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "time": self.formatTime(record),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "line": record.lineno,
        }
        return json.dumps(log_record)

# Установка логгера в зависимости от настроек
def setup_logger():
    logger = logging.getLogger()
    logger.setLevel(log_settings.level)
    
    if log_settings.renderer == "json":
        handler = logging.StreamHandler(sys.stdout)
        formatter = JsonFormatter()
        handler.setFormatter(formatter)
    else:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(f'%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
    
    logger.addHandler(handler)

    # Логирование необработанных исключений
    if log_settings.log_unhandled:
        def handle_exception(exc_type, exc_value, exc_traceback):
            if issubclass(exc_type, KeyboardInterrupt):
                sys.__excepthook__(exc_type, exc_value, exc_traceback)
                return
            logger.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))

        sys.excepthook = handle_exception

    return logger

# Инициализация логгера
logger = setup_logger()
