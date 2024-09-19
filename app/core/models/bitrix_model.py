import structlog
from structlog.typing import FilteringBoundLogger

from ..operations.api.action import action

logger: FilteringBoundLogger = structlog.get_logger()


class BitrixModel:
    def __init__(self, host: str, token: str, get_comments_event: str, get_tasks_event: str, *args) -> None:
        self.host = host
        self.token = token
        self.base_url = f'{host}/rest/72'
        self.get_comments_event = get_comments_event
        self.get_tasks_event = get_tasks_event

    async def _action(self, event: str, **params):
        event_url = event
        if params:
            event_url += '?' + '&'.join(f'{key}={value}' for key, value in params.items())
        
        return await action(self.base_url, self.token, event_url)

    async def get_comments(self, task_id: int):
        return await self._action(self.get_comments_event, id=task_id)

    async def get_tasks(self, start: int = 0):
        return await self._action(self.get_tasks_event, start=start, STATUS='2')