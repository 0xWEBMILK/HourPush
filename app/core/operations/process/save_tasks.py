from .file_utils import load_json_file, save_json_file
from .tasks_processing import get_current_month, process_task_list


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
    existing_data = load_json_file(saves_path, saves_encoding)
    updated_data = process_task_list(tasks, existing_data, month)
    save_json_file(saves_path, updated_data, saves_encoding)