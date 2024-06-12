from fastapi import HTTPException
from fastapi.responses import Response
from ..schemas.response import (
    CreateMemeResp,
    EditMemeResp,
    DelMemeResp,
    GetMemesResp,
    GetMemeResp,
    Meme,
)


class ResponseBuilder:
    @classmethod
    def build(cls, *args, **kwgs):
        raise NotImplementedError()


class CreateMemeRespBuilder(ResponseBuilder):
    @classmethod
    def build(cls, meme_id: int):
        return CreateMemeResp(meme_id=meme_id)


class DelMemeRepBuilder(ResponseBuilder):
    @classmethod
    def build(cls):
        return DelMemeResp()


class EditMemeRespBuilder(ResponseBuilder):
    @classmethod
    def build(cls):
        return EditMemeResp()


class ErrorRespBuilder(ResponseBuilder):
    @classmethod
    def build(cls, msg, status_code=400):
        raise HTTPException(status_code=status_code, detail=msg)


class GetMemesRespBuilder(ResponseBuilder):
    @classmethod
    def build(cls, memes: list[Meme]):
        return GetMemesResp(memes=memes)


class GetMemeRespBuilder(ResponseBuilder):
    @classmethod
    def build(cls, meme: Meme):
        return GetMemeResp(id=meme.id, content=meme.content)


class GetImgRespBuilder(ResponseBuilder):
    @classmethod
    def build(cls, content: bytes):
        return Response(content)
