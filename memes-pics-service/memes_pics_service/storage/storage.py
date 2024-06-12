import logging
from abc import ABC, abstractmethod
from typing import TypeVar
from fastapi import UploadFile
from minio import Minio
from urllib3.response import HTTPResponse
from ..schemas.schemas import StorageImage
from ..settings import SETTINGS


ImgUploaded = TypeVar('ImgUploaded', bound=bool)


class StorageInterface(ABC):
    def init_storage(self):
        raise NotImplementedError()

    @abstractmethod
    def upload(self, img: UploadFile):
        raise NotImplementedError()

    @abstractmethod
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

    async def download(self, img_name: str) -> bytes:
        response: HTTPResponse = self.client.get_object(self.bucket_name, img_name)
        content = response.read()
        return StorageImage(content=content, img_name=img_name)

    async def upload(self, img: UploadFile) -> ImgUploaded:
        try:
            self.client.put_object(self.bucket_name, img.filename, img.file, img.size, img.content_type)
            return True
        except Exception as e:
            logging.error(e, exc_info=True)
            return False

    async def init_storage(self):
        bucket_exists = self.client.bucket_exists(self.bucket_name)
        if not bucket_exists:
            self.client.make_bucket(self.bucket_name)

    @property
    def client(self):
        return self._client
