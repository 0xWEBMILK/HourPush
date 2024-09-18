import pandas as pd

async def json_to_dataframe(data):
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