from typing import Annotated
from fastapi import FastAPI, UploadFile, File
from .service import ServiceDep

app = FastAPI(
    version='1',
    description='Memes Pictures service',
)


@app.post('/upload')
async def upload_img(
    service: ServiceDep,
    img: Annotated[UploadFile, File()],
):
    return await service.upload_img(img)


@app.get('/imgs/{img_name}')
async def download_img(
    img_name: str,
    service: ServiceDep
):
    return await service.download_img(img_name)
