from pydantic import BaseModel


class StorageImage(BaseModel):
    content: bytes
    img_name: str
