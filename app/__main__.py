import asyncio

from core.core import run
from core.config.logger_setup import logger


async def main():
    logger.info('Started!')
    await run()
    logger.info('Stopped!')


if __name__ == "__main__":
    asyncio.run(main())