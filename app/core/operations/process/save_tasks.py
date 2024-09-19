from datetime import datetime
import json
import os

async def save_tasks(tasks: list, saves_path: str, saves_encoding: str) -> None:
    date = datetime.now()
    month = date.strftime('%B')

    if os.path.exists(saves_path):
        with open(saves_path, 'r', encoding=saves_encoding) as file:
            existing_data = json.load(file)
    else:
        existing_data = {}

    if month not in existing_data:
        existing_data[month] = []

    task_dict = {task['title']: task for task in existing_data[month]}

    # Status: 6 _\|/_ Отложена

    for task in tasks:
        if (task.get('status') != '5' and task.get('priority') != '1') or (task.get('status') == '6'):
            if task['title'] in task_dict:
                task_dict[task['title']]['lead-time'] += 24
                task_dict[task['title']]['touch-time'] = task['hour']
            else:
                task_dict[task['title']] = {'title': task.get('title'), 'lead-time': 24, 'touch-time': task['hour']}

    existing_data[month] = list(task_dict.values())

    with open(saves_path, 'w', encoding=saves_encoding) as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)

    with open(saves_path, 'w', encoding=saves_encoding) as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)