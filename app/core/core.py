from .utils.initialise import bitrix_variables_initialise, saves_variables_initialise, database_variables_initialise

import structlog
from structlog.typing import FilteringBoundLogger

from .models import BitrixModel, DatabaseModel
from .operations.get import get_tasks, get_comments
from .operations.process import save_tasks
from .operations.database import save_to_database


logger: FilteringBoundLogger = structlog.get_logger()


async def run(*args, **kwargs):
    logger.info("Variables initialise | started")
    bitrix_config = await bitrix_variables_initialise()
    database_config = await database_variables_initialise()
    saves_config = await saves_variables_initialise()
    logger.info("Variables initialise | success")

    logger.info("Models initialise | started")
    bitrix_model = BitrixModel(
        token=bitrix_config.get('token'),
        host=bitrix_config.get('host'),

        get_comments_event=bitrix_config.get('get_comments_event'),
        get_tasks_event=bitrix_config.get('get_tasks_event')
    )

    database_model = DatabaseModel(
        sqlalchemy_database_uri = database_config.get('sqlalchemy_database_uri'),
        sqlalchemy_track_modifications = database_config.get('sqlalchemy_track_modifications')
    )
    logger.info("Models initialise | success")

    logger.info("Getting all tasks | started")
    bitrix_tasks = await get_tasks(bitrix_model)
    logger.info("Getting all tasks | success")

    logger.info("Calculating hours from comments | started")
    bitrix_tasks = await get_comments(bitrix_model, bitrix_tasks)
    logger.info("Calculating hours from comments | success")

    logger.info("Saving tasks | started")
    await save_tasks(bitrix_tasks,
                     saves_path=saves_config.get('saves_path'),
                     saves_encoding=saves_config.get('saves_encoding'))
    logger.info("Saving tasks | success")

    logger.info("Writing to database | started")
    await save_to_database(database_model,
                           table_name=database_config.get('table_name'),
                           saves_path=saves_config.get('saves_path'))
    logger.info("Writing to database | success")