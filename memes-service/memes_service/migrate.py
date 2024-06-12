import asyncio
from .orm.postgres.con import init_models


async def migrate():
    await init_models()


def main():
    asyncio.run(migrate())
