from ..config_setup import main_settings
from typing import Dict


async def database_variables_initialise() -> Dict[str, str]:
    return {
            "sqlalchemy_database_uri": main_settings.database.sqlalchemy_database_uri.get_secret_value(),
            "sqlalchemy_track_modifications": main_settings.database.sqlalchemy_track_modifications,
            "table_name": main_settings.database.table_name.get_secret_value(),
        }