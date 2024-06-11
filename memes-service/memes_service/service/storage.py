from typing import TypeVar
from ..schemas.schemas import Meme


MemeId = TypeVar('MemeId', bound=int)


class MemeStorage:
    async def get_memes(self) -> list[Meme]:
        return []
