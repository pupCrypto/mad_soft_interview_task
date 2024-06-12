import logging
from typing import Annotated
from fastapi import Depends, UploadFile
from .response_builder import (
    ErrorRespBuilder,
    UploadImgRespBuilder,
    GetImgRespBuilder,
)
from .utils import gen_img_url
from ..storage import MinioStorage


class ErrorMsg:
    CANNOT_UPLOAD_IMG = 'Не удалось сохранить изображение'


class Service:
    def __init__(self):
        self._storage = MinioStorage()

    async def upload_img(self, img: UploadFile):
        uploaded = await self.storage.upload(img)
        if not uploaded:
            return ErrorRespBuilder.build(ErrorMsg.CANNOT_UPLOAD_IMG)
        img_url = gen_img_url(img.filename)
        return UploadImgRespBuilder.build(img_url)

    async def download_img(self, img_name: str):
        img = await self.storage.download(img_name)
        return GetImgRespBuilder.build(img)

    @property
    def storage(self):
        return self._storage


async def get_service():
    service = Service()
    try:
        await service.storage.init_storage()
    except Exception as e:
        logging.error(e, exc_info=True)
    return service

ServiceDep = Annotated[Service, Depends(Service)]
