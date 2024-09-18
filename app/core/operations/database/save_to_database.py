from .load_json import load_json
from .json_to_dataframe import json_to_dataframe


async def save_to_database(database_model, table_name, saves_path):
    data = await load_json(saves_path)
    dataframe = await json_to_dataframe(data)

    await database_model.initialise()
    await database_model.write_to_table(dataframe, table_name)