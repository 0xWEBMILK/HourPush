from pydantic import SecretStr, BaseModel
from decouple import config
from enum import Enum

# Logs settings
class ModeEnum(str, Enum):
    DEVELOPMENT = "dev"
    PRODUCTION = "prod"

class LoggingRenderer(str, Enum):
    JSON = "json"
    CONSOLE = "console"

class LoggingSettings(BaseModel):
    level: str = "INFO"
    format: str = "%Y-%m-%d %H:%M:%S"
    is_utc: bool = False

    renderer: LoggingRenderer = LoggingRenderer.JSON
    log_unhandled: bool = False

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        env_prefix = "LOGGING_"

# Bitrix settings
class BitrixSettings(BaseModel):
    host: SecretStr = SecretStr(config('HOST'))
    token: SecretStr = SecretStr(config('TOKEN'))
    
    get_comments_event: SecretStr = SecretStr(config('GET_COMMENTS_EVENT'))
    get_tasks_event: SecretStr = SecretStr(config('GET_TASKS_EVENT'))
    get_stages_event: SecretStr = SecretStr(config('GET_STAGES_EVENT'))
    get_sprint_event: SecretStr = SecretStr(config('GET_SPRINT_EVENT'))



# Saves settings
class SavesSettings(BaseModel):
    saves_path: SecretStr = SecretStr(config('SAVES_PATH'))
    saves_encoding: SecretStr = SecretStr(config('SAVES_ENCODING'))


# Database settings
class DatabaseSettings(BaseModel):
    sqlalchemy_database_uri: SecretStr = SecretStr(config('SQLALCHEMY_DATABASE_URI'))
    sqlalchemy_track_modifications: bool = config('SQLALCHEMY_TRACK_MODIFICATIONS', cast=bool)
    table_name: SecretStr = SecretStr(config('TABLE_NAME'))

# Main model
class MainSettings(BaseModel):
    saves: SavesSettings = SavesSettings()
    bitrix: BitrixSettings = BitrixSettings()
    database: DatabaseSettings = DatabaseSettings()

    # .env path
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

# Exporting the settings
main_settings = MainSettings()
log_settings = LoggingSettings()