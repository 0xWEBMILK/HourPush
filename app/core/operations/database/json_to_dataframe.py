import pandas as pd

async def json_to_dataframe(data: dict) -> pd.DataFrame:
    """
    Converts a dictionary of tasks by month into a pandas DataFrame.

    Args:
        data (dict): A dictionary where the keys are months and the values are lists of tasks. 
                     Each task is represented as a dictionary with 'title', 'lead-time', and 'touch-time'.

    Returns:
        pd.DataFrame: A DataFrame with columns ['Month', 'Title', 'Lead Time', 'Touch Time'].
    """
    records = []
    
    for month, tasks in data.items():
        for task in tasks:
            record = {
                'Month': month,
                'Title': task['title'],
                'Lead Time': task['lead-time'],
                'Touch Time': task['touch-time']
            }
            records.append(record)
    
    return pd.DataFrame(records)
