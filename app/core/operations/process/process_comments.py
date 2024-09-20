import datetime
import re

async def process_comments(text, date):
    now = datetime.datetime.now()

    if f"{now.strftime("%Y")}-{now.strftime("%m")}" != date[:7]:
        return 0.0
    else:
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

        total_hours = hours + (minutes / 60.0)
        return total_hours
