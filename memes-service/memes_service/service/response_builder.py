from ..schemas.response import (
    GetMemesResp,
    GetMemeResp,
)
from ..schemas.schemas import Meme


class ResponseBuilder:
    @classmethod
    def build(cls, *args, **kwgs):
        raise NotImplementedError()


class GetMemesRespBuilder(ResponseBuilder):
    @classmethod
    def build(cls, memes: list[Meme]):
        return GetMemesResp(memes=memes)


class GetMemeRespBuilder(ResponseBuilder):
    @classmethod
    def build(cls, meme: Meme):
        return GetMemeResp(content=meme.content, img_url=meme.img_url)
