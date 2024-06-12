from pydantic import BaseModel, HttpUrl


class UploadImgResp(BaseModel):
    img_url: HttpUrl
