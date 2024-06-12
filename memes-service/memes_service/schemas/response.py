import enum
from pydantic import BaseModel, ConfigDict


class Meme(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    content: str


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
