import json

async def load_json(file_path: str) -> dict:
    """
    Loads JSON data from a specified file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The loaded JSON data as a dictionary.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)
