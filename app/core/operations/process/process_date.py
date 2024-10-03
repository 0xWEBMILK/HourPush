import datetime

def process_date(date):
    now = datetime.datetime.now().date()
    task_date = datetime.datetime.strptime(date[0:10], '%Y-%m-%d').date()
    print(24 * (now - task_date).days)


process_date("2024-09-26T12:26:16+03:00")