# tasks.api.scrum.sprint.list?filter[STATUS]=active&filter[GROUP_ID]=72
async def get_stages(bitrix_model, bitrix_sprint_id):
    result = await bitrix_model.get_stages(bitrix_sprint_id)

    return result['result'][1:-1]