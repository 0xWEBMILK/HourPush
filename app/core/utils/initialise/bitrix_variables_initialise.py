from ..config_setup import main_settings
from typing import Dict


def bitrix_variables_initialise() -> Dict[str, str]:
    return {
            "host": main_settings.bitrix.host.get_secret_value(),
            "token": main_settings.bitrix.token.get_secret_value(),

            "get_comments_event": main_settings.bitrix.get_comments_event.get_secret_value(),
            "get_tasks_event": main_settings.bitrix.get_tasks_event.get_secret_value(),
            "get_stages_event": main_settings.bitrix.get_stages_event.get_secret_value(),
            "get_sprint_event": main_settings.bitrix.get_sprint_event.get_secret_value(),
        }