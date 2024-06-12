from pydantic import ConfigDict, BaseModel, HttpUrl


class Meme(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    content: str
    img_url: HttpUrl | None = None
