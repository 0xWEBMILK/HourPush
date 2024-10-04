from datetime import datetime


def get_current_month() -> str:
    """
    Returns the current month as a string in full textual format (e.g., 'September').

    Returns:
        str: The name of the current month.
    """

    return datetime.now().strftime('%B')


def process_tasks(tasks: list, existing_data: dict, month: str) -> dict:
    """
    Processes a list of tasks and updates the existing data for the given month.

    Args:
        tasks (list): A list of tasks, where each task is a dictionary containing 'title', 'status', 'priority', and 'hour'.
        existing_data (dict): The current data stored for various months.
        month (str): The current month that is being updated.

    Returns:
        dict: The updated existing data with the processed tasks for the given month.
    """
    
    if month not in existing_data:
        existing_data[month] = []

    task_dict = {task['title']: task for task in existing_data[month]}

    for task in tasks:
        if (task.get('status') != '5' and task.get('priority') != '1') or (task.get('status') == '6'):
            if task['title'] in task_dict:
                task_dict[task['title']]['lead-time'] += 24
                task_dict[task['title']]['touch-time'] = task['hour']
            else:
                task_dict[task['title']] = {'title': task.get('title'), 'lead-time': 24, 'touch-time': task['hour']}

    existing_data[month] = list(task_dict.values())
    return existing_data