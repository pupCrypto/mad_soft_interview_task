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
    GetImgRespBuilder,
)
from .utils import get_pic_upload_url
from ..storage import MemeId, DbMemeStorage
from ..storage.exceptions import MemeNotFound, NoDataToUpdate

ImageUrl = TypeVar('ImageUrl', bound=str)


class ErrorMsg:
    CANNOT_UPLOAD_IMG = 'Не удалось сохранить изображение'
    MEME_NOT_FOUND = 'Мем не был найден'
    NO_DATA_PROVIDED = 'Тело не должно быть пустым'


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

    async def create_meme(self, content: str, img: UploadFile | None):
        img_url = None
        if bool(img):
            img_url = await self.upload_img(img)
            if img_url is None:
                return ErrorRespBuilder.build(ErrorMsg.CANNOT_UPLOAD_IMG, status.HTTP_400_BAD_REQUEST)
        meme_id = await self.storage.create_meme(content, img_url)
        return CreateMemeRespBuilder.build(meme_id)

    async def edit_meme(self, meme_id: MemeId, content: str | None = None, img: UploadFile | None = None):
        img_url = None
        if img is not None:
            img_url = await self.upload_img(img)
        try:
            await self.storage.update_meme(meme_id, content, img_url)
        except MemeNotFound:
            return ErrorRespBuilder.build(ErrorMsg.MEME_NOT_FOUND, status.HTTP_404_NOT_FOUND)
        except NoDataToUpdate:
            return ErrorRespBuilder.build(ErrorMsg.NO_DATA_PROVIDED)
        return EditMemeRespBuilder.build()

    async def del_meme(self, meme_id: MemeId):
        try:
            await self.storage.del_meme(meme_id)
        except MemeNotFound:
            return ErrorRespBuilder.build(ErrorMsg.MEME_NOT_FOUND, status.HTTP_404_NOT_FOUND)
        return DelMemeRepBuilder.build()

    async def upload_img(self, img: UploadFile) -> ImageUrl | None:
        url = get_pic_upload_url()
        response = await self.http_files(url, img=(img.filename, img.file, img.content_type))
        if response.status_code == status.HTTP_200_OK:
            resp_json = response.json()
            return resp_json['img_url']
        return None

    async def get_img(self, meme_id: MemeId):
        try:
            db_meme = await self.storage.get_meme(meme_id)
        except MemeNotFound:
            return ErrorRespBuilder.build(ErrorMsg.MEME_NOT_FOUND, status.HTTP_404_NOT_FOUND)
        response = await self.http_get(db_meme.img_url.unicode_string())
        return GetImgRespBuilder.build(response.content)

    async def http_get(self, url: str) -> httpx.Response:
        async with httpx.AsyncClient() as client:
            return await client.get(url)

    async def http_files(self, url: str, **files) -> httpx.Response:
        async with httpx.AsyncClient() as client:
            return await client.post(url, files=files)

    @property
    def storage(self):
        return self._storage


ServiceDep = Annotated[Service, Depends(Service)]
