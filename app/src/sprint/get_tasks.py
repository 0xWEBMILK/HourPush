async def get_tasks(bitrix_client, active_stage_ids):
    response = [(await bitrix_client.get_tasks(stage_id))['result'] for stage_id in active_stage_ids]
    return response