
from typing import Annotated
from fastapi import Depends
from minio import Minio
from ..settings import SETTINGS


class MinioService:
    bucket_name = 'meme-pics'

    def __init__(self):
        self._client = Minio(
            SETTINGS.MINIO_ENDPOINT,
            access_key=SETTINGS.MINIO_ACCESS_KEY,
            secret_key=SETTINGS.MINIO_SECRET_KEY
        )
        self.init_bucket()

    def save_img(self):
        ...

    def init_bucket(self):
        bucket_exists = self.client.bucket_exists(self.bucket_name)
        if not bucket_exists:
            self.client.make_bucket(self.bucket_name)

    @property
    def client(self):
        return self._client


MinioServiceDep = Annotated[Minio, Depends(MinioService)]
