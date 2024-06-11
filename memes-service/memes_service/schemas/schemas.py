from pydantic import BaseModel, HttpUrl


class Meme(BaseModel):
    content: str
    img_url: HttpUrl
