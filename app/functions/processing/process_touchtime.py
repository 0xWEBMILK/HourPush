import datetime
import re

def process_touchtime(bitrix_tasks):
    now = datetime.datetime.now()

    for bitrix_task in bitrix_tasks:
        total_hours = 0.0

        for comment in bitrix_task['comments']:
            if f"{now.strftime('%Y')}-{now.strftime('%m')}" != comment['POST_DATE'][:7]:
                total_hours = 0.0
            else:
                text = comment['POST_MESSAGE']
                text = re.sub(r'[^\w\s.,]', '', text)

                time_patterns = re.findall(r'(\d+(?:[.,]\d*)?)\s*(час[а-я]*|ч|minут[а-я]*|мин)', text)

                hours = 0.0
                minutes = 0.0

                for amount, unit in time_patterns:
                    try:
                        amount = float(amount.replace(',', '.'))
                        if re.search(r'час[а-я]*|ч', unit):
                            hours += amount
                        elif re.search(r'минут[а-я]*|мин', unit):
                            minutes += amount
                    except:
                        pass

                total_hours += hours + (minutes / 60.0)

        bitrix_task['touch-time'] = total_hours

    return bitrix_tasks

