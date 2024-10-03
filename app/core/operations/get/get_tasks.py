async def get_tasks(bitrix_model, bitrix_stage_ids):
    list_of_tasks = []

    for bitrix_id in bitrix_stage_ids:
        response = await bitrix_model.get_tasks(bitrix_id=bitrix_id["id"])

        tasks = response.get('result', {}).get('tasks', [])
        print(tasks)

        list_of_tasks.extend({**task, 'hour': 0.0} for task in tasks)

    return list_of_tasks
