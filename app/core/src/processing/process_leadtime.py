import re
import datetime


def process_leadtime(bitrix_tasks):
    current_date = datetime.datetime.now().date()

    for task in bitrix_tasks:
        for comment in task['comments']:
            try:
                task_created_date = datetime.datetime.strptime(re.findall(r"\d{4}\-\d{2}\-\d{2}", comment.get('POST_MESSAGE'))[0], "%Y-%m-%d").date()
                break
            except IndexError:
                task_created_date = datetime.datetime.strptime("0001-01-01", "%Y-%m-%d").date()

        lead_time = (current_date - task_created_date).days
        task['lead-time'] = lead_time * 24