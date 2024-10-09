from decouple import config
from pydantic import SecretStr

def get_db_config():
    return {
        'SQLALCHEMY_DATABASE_URI': SecretStr(config('SQLALCHEMY_DATABASE_URI')),
        'SQLALCHEMY_TRACK_MODIFICATIONS': config('SQLALCHEMY_TRACK_MODIFICATIONS', cast=bool),
        'TABLE_NAME': SecretStr(config('TABLE_NAME')),
    }
