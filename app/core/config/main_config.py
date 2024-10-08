from .bitrix_config import get_bitrix_config
from .db_config import get_db_config
from .logging_config import get_logging_config

def get_all_configs():
    return {
        'bitrix': get_bitrix_config(),
        'database': get_db_config(),
        'logging': get_logging_config(),
    }