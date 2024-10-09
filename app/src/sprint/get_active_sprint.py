async def get_active_sprint(bitrix_client):
    response = await bitrix_client.get_sprint()
    return response['result'][0]['id']