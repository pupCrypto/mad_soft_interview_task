from typing import Annotated
from fastapi import Depends
from .response_builder import (
    GetMemesRespBuilder,
    GetMemeRespBuilder,
)
from .storage import MemeStorage, MemeId
from ..schemas.request import (
    CreateMemeReq,
    EditMemeReq,
)


class Service:
    def __init__(self) -> None:
        self.storage = MemeStorage()

    async def get_memes(self):
        memes = await self.storage.get_memes()
        return GetMemesRespBuilder.build(memes)

    async def get_meme(self, meme_id: MemeId):
        meme = await self.storage.get_meme(meme_id)
        return GetMemeRespBuilder.build(meme)

    async def create_meme(self, params: CreateMemeReq):
        ...

    async def edit_meme(self, params: EditMemeReq):
        ...

    async def del_meme(self, meme_id: MemeId):
        ...


ServiceDep = Annotated[Service, Depends(Service)]
