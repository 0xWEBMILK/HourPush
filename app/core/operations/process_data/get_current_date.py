from datetime import datetime


def get_current_month() -> str:
    """
    Returns the current month as a string in full textual format (e.g., 'September').

    Returns:
        str: The name of the current month.
    """

    return datetime.now().strftime('%B')
