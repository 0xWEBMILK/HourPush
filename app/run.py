import asyncio

import structlog
from structlog.typing import FilteringBoundLogger

from core.utils.logger_setup import get_structlog_config
from core.utils.config_setup import log_settings

from core import run


logger: FilteringBoundLogger = structlog.get_logger()


async def main():
    structlog.configure(**get_structlog_config(log_settings))

    await logger.awarning('Started')
    await run()
    await logger.awarning('Stopped')

if __name__ == "__main__":
    asyncio.run(main())