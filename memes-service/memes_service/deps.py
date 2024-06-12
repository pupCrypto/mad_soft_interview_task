from typing import Annotated
from fastapi import Depends
from minio import Minio
from .settings import SETTINGS


def get_minio_client():
    return Minio(
        SETTINGS.MINIO_ENDPOINT,
        access_key=SETTINGS.MINIO_ACCESS_KEY,
        secret_key=SETTINGS.MINIO_SECRET_KEY
    )


MinioDep = Annotated[Minio, Depends(get_minio_client)]