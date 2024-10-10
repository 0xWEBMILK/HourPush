async def get_stages(bitrix_client, active_sprint_id):
    response = await bitrix_client.get_stages(active_sprint_id)

    return [stage['id'] for stage in response['result'][1:-1]]