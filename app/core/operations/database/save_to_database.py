from .load_json import load_json
from .json_to_dataframe import json_to_dataframe

async def save_to_database(database_model, table_name: str, saves_path: str) -> None:
    """
    Loads data from a JSON file, converts it to a DataFrame, and writes it to the specified database table.

    Args:
        database_model: The database model instance responsible for managing the database.
        table_name (str): The name of the table where the data will be written.
        saves_path (str): The path to the JSON file containing the data.

    Returns:
        None
    """
    data = await load_json(saves_path)
    dataframe = await json_to_dataframe(data)

    await database_model.initialise()
    await database_model.write_to_table(dataframe, table_name)
