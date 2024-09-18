from ..process import process_comments

async def get_comments(bitrix_model, tasks):
    for task in tasks:
            response = await bitrix_model.get_comments(task_id=task["id"])

            for comment in response['result']:
                task['hour'] = task['hour'] + await process_comments(comment['POST_MESSAGE'], comment['POST_DATE'])

    return tasks