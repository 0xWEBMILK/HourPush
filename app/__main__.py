import asyncio

from config.logger_setup import logger

from config.logger_setup import logger
from config.main_config import get_all_configs

from functions.api.bitrix_client import BitrixClient
from functions.sprint import get_active_sprint, get_stages, get_tasks, get_comments
from functions.processing import process_leadtime, process_touchtime
from functions.db.database import Database


async def main(*args, **kwargs):
    logger.info("Initialise variables | Started")
    bitrix_config = get_all_configs()['bitrix']
    database_config = get_all_configs()['database']
    logger.info("Initialise variables | Success")

    logger.info("Initialising client | Started")
    bitrix_client = BitrixClient(bitrix_config['HOST'],
                                 bitrix_config['TOKEN'].get_secret_value(),
                                 bitrix_config['GET_COMMENTS_EVENT'],
                                 bitrix_config['GET_STAGES_EVENT'],
                                 bitrix_config['GET_SPRINT_EVENT'],
                                 bitrix_config['GET_TASKS_EVENT'])
    db = Database(
        database_url=database_config['SQLALCHEMY_DATABASE_URI'].get_secret_value(),
        table_name=database_config['TABLE_NAME'].get_secret_value()
    )
    logger.info("Initialising client | Success")

    logger.info("Getting active sprint | Started")
    active_sprint_id = await get_active_sprint(bitrix_client)
    logger.info("Getting active sprint | Success")

    logger.info("Getting stages from active sprint | Started")
    active_stage_ids = await get_stages(bitrix_client, active_sprint_id)
    logger.info("Getting stages from active sprint | Success")

    logger.info("Getting tasks from stages | Started")
    bitrix_tasks = await get_tasks(bitrix_client, active_stage_ids)
    logger.info("Getting tasks from stages | Success")

    logger.info("Getting comments from tasks | Started")
    bitrix_tasks = await get_comments(bitrix_client, bitrix_tasks)
    logger.info("Getting comments from tasks | Success")

    logger.info("Processing lead-time | Started")
    bitrix_tasks = process_leadtime(bitrix_tasks)
    logger.info("Processing lead-time | Success")

    logger.info("Processing touch-time | Started")
    bitrix_tasks = process_touchtime(bitrix_tasks)
    logger.info("Processing touch-time | Success")

    logger.info("Saving tasks to database | Started")
    db.save_tasks(bitrix_tasks)
    logger.info("Saving tasks to database | Success")

if __name__ == "__main__":
    asyncio.run(main())