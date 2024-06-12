from typing import Annotated
from fastapi import Depends, UploadFile
from minio import Minio
from ..settings import SETTINGS


class MinioService:
    bucket_name = 'meme-pics'

    def __init__(self):
        self._client = Minio(
            endpoint=SETTINGS.MINIO_ENDPOINT,
            access_key=SETTINGS.MINIO_ACCESS_KEY,
            secret_key=SETTINGS.MINIO_SECRET_KEY,
            secure=False
        )

    def save_img(self, img: UploadFile):
        self.client.put_object(self.bucket_name, img.filename, img.file, img.size)

    def init_bucket(self):
        bucket_exists = self.client.bucket_exists(self.bucket_name)
        if not bucket_exists:
            self.client.make_bucket(self.bucket_name)

    @property
    def client(self):
        return self._client


def get_minio_client():
    client = MinioService()
    try:
        client.init_bucket()
    except:
        pass
    return client


MinioServiceDep = Annotated[MinioService, Depends(get_minio_client)]
