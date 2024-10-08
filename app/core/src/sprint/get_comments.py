async def get_comments(bitrix_client, bitrix_tasks):
    tasks_with_comments = []

    for bitrix_task in bitrix_tasks:
        for bitrix_task_id in bitrix_task['tasks']:
            comments = await bitrix_client.get_comments(bitrix_task_id['id'])
            tasks_with_comments.append({
                'task_id': bitrix_task_id['id'],
                'title': bitrix_task_id['title'],
                'createdDate': bitrix_task_id['createdDate'],
                'comments': comments['result']
            })

    return tasks_with_comments
