from typing import List, Dict


async def get_tasks(bitrix_model, bitrix_stage_ids: List[Dict]) -> List[Dict]:
    """
    Retrieves tasks for a list of stage IDs from the Bitrix model and initializes each task's 'hour' field to 0.0.

    Args:
        bitrix_model: The Bitrix model instance used to fetch the tasks.
        bitrix_stage_ids (List[Dict]): A list of dictionaries containing stage IDs with at least an 'id' key.

    Returns:
        List[Dict]: A list of tasks where each task is extended with an additional 'hour' field initialized to 0.0.
    """
    list_of_tasks = []

    # Fetch tasks for each stage ID and initialize their 'hour' to 0.0
    for bitrix_id in bitrix_stage_ids:
        response = await bitrix_model.get_tasks(bitrix_id=bitrix_id["id"])

        # Extract tasks and set 'hour' to 0.0 for each task
        tasks = response.get('result', {}).get('tasks', [])
        list_of_tasks.extend({**task, 'hour': 0.0} for task in tasks)

    return list_of_tasks
