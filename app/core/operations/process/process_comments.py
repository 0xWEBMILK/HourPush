from typing import Union
import datetime
import re

async def process_comments(text: str, date: str) -> float:
    """
    Processes a text to extract time-related patterns and calculates the total time in hours. 
    Returns 0.0 if the date provided does not match the current month.

    Args:
        text (str): The comment text that may contain time-related information.
        date (str): A string representing the date in the format 'YYYY-MM-DD' or similar.

    Returns:
        float: The total time in hours extracted from the text, or 0.0 if the date is outside the current month.
    """
    now = datetime.datetime.now()

    # Check if the date is in the current year and month
    if f"{now.strftime('%Y')}-{now.strftime('%m')}" != date[:7]:
        return 0.0
    else:
        text = re.sub(r'[^\w\s.,]', '', text)

        # Find all time patterns (hours or minutes)
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