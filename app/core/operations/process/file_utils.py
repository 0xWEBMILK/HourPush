import json
import os


def load_json_file(file_path: str, encoding: str) -> dict:
    """
    Loads JSON data from a specified file.

    Args:
        file_path (str): The path to the file containing JSON data.
        encoding (str): The encoding format used to open the file.

    Returns:
        dict: The data from the JSON file. Returns an empty dictionary if the file does not exist.
    """
    
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding=encoding) as file:
            return json.load(file)
    return {}


def save_json_file(file_path: str, data: dict, encoding: str) -> None:
    """
    Saves JSON data to a specified file.

    Args:
        file_path (str): The path to the file where JSON data will be saved.
        data (dict): The data to be written to the file.
        encoding (str): The encoding format used to write the file.
    
    Returns:
        None
    """

    with open(file_path, 'w', encoding=encoding) as file:
        json.dump(data, file, ensure_ascii=False, indent=4)