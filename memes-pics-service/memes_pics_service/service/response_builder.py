from fastapi import HTTPException
from fastapi.responses import Response
from ..schemas.response import (
    UploadImgResp,
)
from ..schemas.schemas import StorageImage


class ResponseBuilder:
    @classmethod
    def build(cls, *args, **kwgs):
        raise NotImplementedError()


class ErrorRespBuilder(ResponseBuilder):
    @classmethod
    def build(cls, msg, status_code=400):
        raise HTTPException(status_code=status_code, detail=msg)


class UploadImgRespBuilder(ResponseBuilder):
    @classmethod
    def build(cls, img_url: str):
        return UploadImgResp(img_url=img_url)


class GetImgRespBuilder(ResponseBuilder):
    @classmethod
    def build(cls, img: StorageImage):
        return Response(content=img.content)
