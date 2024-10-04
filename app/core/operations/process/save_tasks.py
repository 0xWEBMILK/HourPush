from .file_methods import load_json_data, save_json_data
from .process_tasks import get_current_month, process_tasks


async def save_tasks(tasks: list, saves_path: str, saves_encoding: str) -> None:
    """
    Saves a list of tasks to a file by processing them and updating the existing data.

    Args:
        tasks (list): A list of tasks, where each task is a dictionary containing 'title', 'status', 'priority', and 'hour'.
        saves_path (str): The path to the file where tasks data will be saved.
        saves_encoding (str): The encoding format used to open and write the file.

    Returns:
        None
    """

    month = get_current_month()
    existing_data = load_json_data(saves_path, saves_encoding)
    updated_data = process_tasks(tasks, existing_data, month)
    save_json_data(saves_path, updated_data, saves_encoding)