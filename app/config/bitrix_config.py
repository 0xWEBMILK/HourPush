from decouple import config
from pydantic import SecretStr

def get_bitrix_config():
    return {
        'HOST': config('HOST'),
        'TOKEN': SecretStr(config('TOKEN')),
        'GET_COMMENTS_EVENT': config('GET_COMMENTS_EVENT'),
        'GET_TASKS_EVENT': config('GET_TASKS_EVENT'),
        'GET_STAGES_EVENT': config('GET_STAGES_EVENT'),
        'GET_SPRINT_EVENT': config('GET_SPRINT_EVENT'),
    }
