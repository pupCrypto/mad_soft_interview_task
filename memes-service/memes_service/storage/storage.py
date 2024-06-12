from abc import ABC, abstractmethod
from typing import TypeVar
from .exceptions import MemeNotFound
from .utils import clear_data
from ..orm.postgres.manager import MemeManager
from ..schemas.schemas import Meme


ImgUrl = TypeVar('ImgUrl', bound=str)
MemeContent = TypeVar('MemeContent', bound=str)
MemeId = TypeVar('MemeId', bound=int)


class MemeStorageInterface(ABC):
    @abstractmethod
    async def get_memes(self) -> list[Meme]:
        """Returns list of memes"""
        raise NotImplementedError()

    @abstractmethod
    async def get_meme(self, meme_id: MemeId) -> Meme:
        """Returns the meme"""
        raise NotImplementedError()

    @abstractmethod
    async def create_meme(self, content: MemeContent, img_url: ImgUrl) -> MemeId:
        """Creates and saves meme"""
        raise NotImplementedError()

    @abstractmethod
    async def update_meme(
        self,
        meme_id: MemeId,
        content: MemeContent | None = None,
        img_url: ImgUrl | None = None
    ):
        """Updates meme"""
        raise NotImplementedError()

    @abstractmethod
    async def del_meme(self, meme_id: MemeId):
        """Delete meme"""
        raise NotImplementedError()


class DbMemeStorage(MemeStorageInterface):
    def __init__(self):
        self._db_manager = MemeManager()

    async def get_memes(self, limit: int = 10, page: int = 0) -> list[Meme]:
        db_memes = await self.manager.get_memes(limit, page)
        return [Meme.model_validate(db_meme) for db_meme in db_memes]

    async def get_meme(self, meme_id: MemeId) -> Meme:
        db_meme = await self.manager.get_meme(meme_id)
        if db_meme is None:
            raise MemeNotFound()
        return Meme.model_validate(db_meme)

    async def create_meme(self, content: MemeContent, img_url: ImgUrl | None = None) -> MemeId:
        meme_id = await self.manager.create_meme(content, img_url)
        return meme_id

    async def update_meme(
            self,
            meme_id: MemeId,
            content: MemeContent | None = None,
            img_url: ImgUrl | None = None
    ):
        data = clear_data(content=content, img_url=img_url)
        is_updated = await self.manager.update_meme(meme_id, **data)
        if is_updated is False:
            raise MemeNotFound()

    async def del_meme(self, meme_id: MemeId):
        is_deleted = await self.manager.del_meme(meme_id)
        if is_deleted is False:
            raise MemeNotFound()

    @property
    def manager(self):
        return self._db_manager
