from typing import TypeVar
from sqlalchemy import delete, update, insert, true, select, ScalarResult
from .con import session as async_session
from .models import Meme

MemeId = TypeVar('MemeId', bound=int)
IsDeleted = TypeVar('IsDeleted', bound=bool)
IsUpdated = TypeVar('IsUpdated', bound=bool)


class MemeManager:
    async def get_memes(self, limit: int = 10, page: int = 0) -> ScalarResult[Meme]:
        async with async_session() as session:
            offset = limit * page
            sql = select(Meme).offset(offset).limit(limit).order_by(Meme.id)
            cursor = await session.execute(sql)
            return cursor.scalars()

    async def get_meme(self, meme_id: MemeId) -> Meme | None:
        async with async_session() as session:
            sql = select(Meme).where(Meme.id == meme_id)
            cursor = await session.execute(sql)
            return cursor.scalar_one_or_none()

    async def create_meme(self, content: str, img_url: str | None) -> MemeId:
        async with async_session() as session:
            sql = insert(Meme).values(content=content, img_url=img_url).returning(Meme.id)
            cursor = await session.execute(sql)
            await session.commit()
            return cursor.scalar_one()

    async def update_meme(self, meme_id: MemeId, **kwgs) -> IsUpdated:
        async with async_session() as session:
            sql = update(Meme).values(**kwgs).where(Meme.id == meme_id).returning(true())
            cursor = await session.execute(sql)
            await session.commit()
            is_updated = cursor.scalar_one_or_none()
            return is_updated is True

    async def del_meme(self, meme_id: MemeId) -> IsDeleted:
        async with async_session() as session:
            sql = delete(Meme).where(Meme.id == meme_id).returning(true())
            cursor = await session.execute(sql)
            await session.commit()
            is_deleted = cursor.scalar_one_or_none()
            return is_deleted is True
