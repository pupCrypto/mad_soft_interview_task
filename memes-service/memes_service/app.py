from fastapi import FastAPI
from .service.service import ServiceDep
from .schemas.request import (
    CreateMemeReq,
    EditMemeReq,
)
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
    service: ServiceDep
) -> GetMemesResp:
    return await service.get_memes()


@app.get('/memes/{meme_id}')
async def get_meme(
    service: ServiceDep,
    meme_id: int
) -> GetMemeResp:
    return await service.get_meme(meme_id)


@app.post('/memes')
async def create_meme(
    service: ServiceDep,
    params: CreateMemeReq,
) -> CreateMemeResp:
    return await service.create_meme(params)


@app.put('/memes/{meme_id}')
async def edit_meme(
    service: ServiceDep,
    meme_id: int,
    params: EditMemeReq,
) -> EditMemeResp:
    return await service.edit_meme(meme_id, params)


@app.delete('/memes/{meme_id}')
async def del_meme(
    service: ServiceDep,
    meme_id: int
) -> DelMemeResp:
    return await service.del_meme(meme_id)