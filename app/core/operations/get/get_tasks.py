async def get_tasks(bitrix_model):
    list_of_tasks, start = [], 0

    while True:
        response = await bitrix_model.get_tasks(start=start)

        tasks = response.get('result', {}).get('tasks', [])
        if not tasks:
            break

        list_of_tasks.extend({**task, 'hour': 0.0} for task in tasks)
        start += 50

    return list_of_tasks
