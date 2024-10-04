from ..config_setup import main_settings
from typing import Dict


def saves_variables_initialise() -> Dict[str, str]:
    return {
            "saves_path": main_settings.saves.saves_path.get_secret_value(),
            "saves_encoding": main_settings.saves.saves_encoding.get_secret_value(),
        }