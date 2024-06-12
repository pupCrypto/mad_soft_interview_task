from pydantic import BaseModel, HttpUrl


class CreateMemeReq(BaseModel):
    content: str
    img_url: HttpUrl | None = None


class EditMemeReq(BaseModel):
    content: str
    img_url: HttpUrl | None = None
