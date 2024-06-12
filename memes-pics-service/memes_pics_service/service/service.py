from typing import Annotated
from fastapi import Depends, UploadFile
from ..storage import MinioStorage


class Service:
    def __init__(self):
        self._storage = MinioStorage()

    async def upload_img(img: UploadFile):
        ...

    async def download_img(img_name: str):
        ...

    @property
    def storage(self):
        return self._storage


async def get_service():
    service = Service()
    try:
        await service.storage.init_storage()
    except Exception as e:
        ...
    return service

ServiceDep = Annotated[Service, Depends(Service)]
