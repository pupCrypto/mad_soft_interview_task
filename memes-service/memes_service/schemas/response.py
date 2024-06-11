import enum
from pydantic import BaseModel
from .schemas import Meme


class Status(enum.Enum):
    OK = 'ok'
    ERROR = 'error'


class BaseResp(BaseModel):
    status: Status = Status.OK


class GetMemesResp(BaseResp):
    memes: list[Meme]


class GetMemeResp(BaseResp, Meme):
    pass


class CreateMemeResp(BaseResp):
    meme_id: int


class EditMemeResp(BaseResp):
    pass


class DelMemeResp(BaseResp):
    pass
