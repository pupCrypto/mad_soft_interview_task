from typing import Annotated, TypeVar
import httpx
from fastapi import Depends, status, UploadFile
from .response_builder import (
    CreateMemeRespBuilder,
    EditMemeRespBuilder,
    ErrorRespBuilder,
    DelMemeRepBuilder,
    GetMemesRespBuilder,
    GetMemeRespBuilder,
)
from ..storage import MemeId, DbMemeStorage
from ..storage.exceptions import MemeNotFound
from ..schemas.request import (
    EditMemeReq,
)
from ..settings import SETTINGS

ImageUrl = TypeVar('ImageUrl', bound=str)


class ErrorMsg:
    CANNOT_UPLOAD_IMG = 'Не сохранить изображение'
    MEME_NOT_FOUND = 'Мем не был найден'


class Service:
    def __init__(self) -> None:
        self._storage = DbMemeStorage()

    async def get_memes(self, limit: int = 10, page: int = 0):
        memes = await self.storage.get_memes(limit, page)
        return GetMemesRespBuilder.build(memes)

    async def get_meme(self, meme_id: MemeId):
        try:
            meme = await self.storage.get_meme(meme_id)
        except MemeNotFound:
            return ErrorRespBuilder.build(ErrorMsg.MEME_NOT_FOUND, status.HTTP_404_NOT_FOUND)
        return GetMemeRespBuilder.build(meme)

    async def create_meme(self, content: str, img: UploadFile):
        img_url = await self.upload_img(img)
        if img_url is None:
            return ErrorRespBuilder.build(ErrorMsg.CANNOT_UPLOAD_IMG, status.HTTP_400_BAD_REQUEST)
        meme_id = await self.storage.create_meme(content, img_url)
        return CreateMemeRespBuilder.build(meme_id)

    async def edit_meme(self, meme_id: MemeId, params: EditMemeReq):
        try:
            await self.storage.update_meme(meme_id, params.content, params.img_url.unicode_string())
        except MemeNotFound:
            return ErrorRespBuilder.build(ErrorMsg.MEME_NOT_FOUND, status.HTTP_404_NOT_FOUND)
        return EditMemeRespBuilder.build()

    async def del_meme(self, meme_id: MemeId):
        try:
            await self.storage.del_meme(meme_id)
        except MemeNotFound:
            return ErrorRespBuilder.build(ErrorMsg.MEME_NOT_FOUND, status.HTTP_404_NOT_FOUND)
        return DelMemeRepBuilder.build()

    async def upload_img(self, img: UploadFile) -> ImageUrl | None:
        url = 'http://' + SETTINGS.IMG_SERVICE_HOST + '/upload'
        async with httpx.AsyncClient() as client:
            response = await client.post(url, files=img)
            if response.status_code == status.HTTP_200_OK:
                resp_json = response.json()
                return resp_json['img_url']
            return None

    @property
    def storage(self):
        return self._storage


ServiceDep = Annotated[Service, Depends(Service)]
