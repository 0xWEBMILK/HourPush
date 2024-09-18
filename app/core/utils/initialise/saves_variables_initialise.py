from ..config_setup import main_settings


async def saves_variables_initialise() -> dict:
    return {
            "saves_path": main_settings.saves.saves_path.get_secret_value(),
            "saves_encoding": main_settings.saves.saves_encoding.get_secret_value(),
        }