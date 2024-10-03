# tasks.api.scrum.sprint.list?filter[STATUS]=active&filter[GROUP_ID]=72
async def get_sprint(bitrix_model):
    result = await bitrix_model.get_sprint()

    return result['result'][0]['id']