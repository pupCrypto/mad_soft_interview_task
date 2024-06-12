
from typing import Annotated
from fastapi import FastAPI, Query, Form, UploadFile, File
from .service.service import ServiceDep
from .schemas.response import (
    GetMemesResp,
    GetMemeResp,
    CreateMemeResp,
    EditMemeResp,
    DelMemeResp,
)


app = FastAPI(
    version='1',
    description='REST Full API memes service'
)


@app.get('/memes')
async def get_memes(
    service: ServiceDep,
    limit: Annotated[int, Query(ge=10, le=50)] = 10,
    page: Annotated[int, Query(ge=0)] = 0
) -> GetMemesResp:
    return await service.get_memes(limit, page)


@app.get('/memes/{meme_id}')
async def get_meme(
    service: ServiceDep,
    meme_id: int
) -> GetMemeResp:
    return await service.get_meme(meme_id)


@app.post('/memes')
async def create_meme(
    service: ServiceDep,
    content: Annotated[str, Form()],
    img: Annotated[UploadFile, File()],
) -> CreateMemeResp:
    return await service.create_meme(content, img)


@app.put('/memes/{meme_id}')
async def edit_meme(
    service: ServiceDep,
    meme_id: int,
    content: Annotated[str | None, Form()] = None,
    img: Annotated[UploadFile | None, File()] = None,
) -> EditMemeResp:
    return await service.edit_meme(meme_id, content, img)


@app.delete('/memes/{meme_id}')
async def del_meme(
    service: ServiceDep,
    meme_id: int
) -> DelMemeResp:
    return await service.del_meme(meme_id)


@app.get('/memes/{meme_id}/img')
async def get_img(
    service: ServiceDep,
    meme_id: int
):
    return await service.get_img(meme_id)
