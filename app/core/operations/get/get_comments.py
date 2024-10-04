from ..process import process_comments
from typing import List, Dict


async def get_comments(bitrix_model, tasks: List[Dict]) -> List[Dict]:
    """
    Fetches comments for each task from the Bitrix model and calculates the total time (in hours) 
    for each task based on the content of the comments.

    Args:
        bitrix_model: The Bitrix model instance used to fetch the comments.
        tasks (List[Dict]): A list of tasks where each task is a dictionary with at least an 'id' and 'hour'.

    Returns:
        List[Dict]: The updated list of tasks with accumulated time (in 'hour') for each task based on the comments.
    """
    for task in tasks:
        # Get comments for the current task
        response = await bitrix_model.get_comments(task_id=task["id"])

        # Process each comment to calculate hours and add it to the task's 'hour'
        for comment in response['result']:
            task['hour'] = task['hour'] + await process_comments(comment['POST_MESSAGE'], comment['POST_DATE'])

    return tasks
