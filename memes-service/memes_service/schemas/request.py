from typing import Annotated
from fastapi import UploadFile, File, Form
from pydantic import BaseModel, HttpUrl


class CreateMemeReq(BaseModel):
    img: Annotated[UploadFile, File()]
    content: Annotated[str, Form()]


class EditMemeReq(BaseModel):
    content: str
    img_url: HttpUrl | None = None
