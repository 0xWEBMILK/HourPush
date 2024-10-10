import aiohttp
import asyncio
from decouple import config
from pydantic import SecretStr
from typing import Dict, Any
from config.logger_setup import logger

class BitrixClient:
    def __init__(self, host: str, token: str, get_comments_event: str, get_stages_event: str, get_sprint_event: str, get_tasks_event: str) -> None:
        self.host = host
        self.token = token
        self.get_comments_event = get_comments_event
        self.get_stages_event = get_stages_event
        self.get_sprint_event = get_sprint_event
        self.get_tasks_event = get_tasks_event

        self.base_url = f"https://{self.host}/rest/72/{self.token}/"
        self.headers = {
            'Content-Type': 'application/json'
        }

    async def _fetch(self, session: aiohttp.ClientSession, url: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """Основной метод для выполнения GET запросов"""
        try:
            async with session.get(url, headers=self.headers, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    return data
                else:
                    logger.error(f"Failed to fetch data from {url}. Status: {response.status}")
                    return {}
        except Exception as e:
            logger.error(f"Error while fetching data from {url}: {e}")
            return {}

    async def get_sprint(self) -> Dict[str, Any]:
        """Метод для получения активного спринта"""
        url = self.base_url + self.get_sprint_event
        async with aiohttp.ClientSession() as session:
            return await self._fetch(session, url)

    async def get_stages(self, sprint_id: int) -> Dict[str, Any]:
        """
        Метод для получения стадий задач, используя ID спринта.
        :param sprint_id: ID спринта, который необходимо передать в запрос
        """
        url = f"{self.base_url}{self.get_stages_event}?sprintId={sprint_id}"
        async with aiohttp.ClientSession() as session:
            return await self._fetch(session, url)

    async def get_tasks(self, stage_id: int) -> Dict[str, Any]:
        """
        Метод для получения задач с конкретной стадии.
        :param stage_id: ID стадии, по которой нужно получить задачи
        """
        url = f"{self.base_url}{self.get_tasks_event}?filter[STAGE_ID]={stage_id}"
        async with aiohttp.ClientSession() as session:
            return await self._fetch(session, url)

    async def get_comments(self, task_id: int) -> Dict[str, Any]:
        """Метод для получения комментариев к задаче по ID задачи"""
        url = f"{self.base_url}{self.get_comments_event}"
        params = {'TASK_ID': task_id}
        async with aiohttp.ClientSession() as session:
            return await self._fetch(session, url, params=params)