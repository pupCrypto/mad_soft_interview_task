from typing import Annotated
from fastapi import Depends


class Service:
    async def get_memes(self):
        return [1, 2, 3]


ServiceDep = Annotated[Service, Depends(Service)]
