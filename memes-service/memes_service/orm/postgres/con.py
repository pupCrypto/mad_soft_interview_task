from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from .models import Base
from memes_service.settings import SETTINGS

engine = create_async_engine(SETTINGS.DATABASE_URL)


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@asynccontextmanager
async def session():
    async with AsyncSession(engine) as session:
        yield session
