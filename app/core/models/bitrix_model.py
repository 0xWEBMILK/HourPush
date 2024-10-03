import structlog
from structlog.typing import FilteringBoundLogger

from ..operations.api.action import action

logger: FilteringBoundLogger = structlog.get_logger()


class BitrixModel:
    def __init__(self,
                 host: str,
                 token: str,
                 get_comments_event: str,
                 get_tasks_event: str,
                 get_stages_event: str,
                 get_sprint_event: str, *args) -> None:
        
        self.host = host
        self.token = token
        self.base_url = f'{host}/rest/72'
        self.get_comments_event = get_comments_event
        self.get_tasks_event = get_tasks_event
        self.get_stages_event = get_stages_event
        self.get_sprint_event = get_sprint_event


    async def _action(self, event: str, **params):
        event_url = event
        if params:
            query_params = []
            for key, value in params.items():
                if isinstance(value, dict):
                    # Обрабатываем вложенные словари
                    for sub_key, sub_value in value.items():
                        query_params.append(f'{key}[{sub_key}]={sub_value}')
                else:
                    # Обрабатываем простые параметры
                    query_params.append(f'{key}={value}')
            
            event_url += '?' + '&'.join(query_params)

        return await action(self.base_url, self.token, event_url)

    

    async def get_comments(self, task_id: int):
        return await self._action(self.get_comments_event, id=task_id)


    async def get_tasks(self, bitrix_id):
        return await self._action(self.get_tasks_event, filter={"STAGE_ID": bitrix_id})

    
    async def get_sprint(self):
        return await self._action(self.get_sprint_event)


    async def get_stages(self, sprint_id):
        return await self._action(self.get_stages_event, sprintId=sprint_id)