from abc import ABC, abstractmethod
from fastapi import UploadFile
from minio import Minio
from ..settings import SETTINGS


class StorageInterface(ABC):
    def init_storage(self):
        raise NotImplementedError()

    @abstractmethod()
    def upload(self, img: UploadFile):
        raise NotImplementedError()

    @abstractmethod()
    def download(self, img_name: str):
        raise NotImplementedError()


class MinioStorage(StorageInterface):
    bucket_name = 'meme-pics'

    def __init__(self):
        self._client = Minio(
            endpoint=SETTINGS.MINIO_ENDPOINT,
            access_key=SETTINGS.MINIO_ACCESS_KEY,
            secret_key=SETTINGS.MINIO_SECRET_KEY,
            secure=False
        )

    async def download(self, img_name: str):
        return super().download(img_name)

    async def upload(self, img: UploadFile):
        return super().upload(img)

    async def init_storage(self):
        bucket_exists = await self.client.bucket_exists(self.bucket_name)
        if not bucket_exists:
            await self.client.make_bucket(self.bucket_name)

    @property
    def client(self):
        return self._client
