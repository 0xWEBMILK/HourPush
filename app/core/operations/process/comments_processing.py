import re
import datetime


def clean_text(text: str) -> str:
    """Clearing text from unnecessary characters."""
    return re.sub(r'[^\w\s.,]', '', text)


def extract_time_patterns(text: str):
    """Look for time patterns in the text and return a list of found values."""
    return re.findall(r'(\d+(?:[.,]\d*)?)\s*(час(?:[а-я]*)|ч|minут(?:[а-я]*)|мин)', text)


def calculate_total_hours(time_patterns) -> float:
    """Calculate the total number of hours by converting minutes to hours."""
    hours = 0.0
    minutes = 0.0

    for amount, unit in time_patterns:
        try:
            amount = float(amount.replace(',', '.'))
            if 'час' in unit or 'ч' in unit:
                hours += amount
            elif 'мин' in unit:
                minutes += amount
        except ValueError:
            pass

    return hours + (minutes / 60.0)

async def process_comment_time(text: str, date: str) -> float:
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

    if f"{now.strftime("%Y")}-{now.strftime("%m")}" != date[:7]:
            return 0.0
    else:
        clean_text_data = clean_text(text)

        time_patterns = extract_time_patterns(clean_text_data)

        total_hours = calculate_total_hours(time_patterns)

        return total_hours
