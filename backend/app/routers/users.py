from typing import Union

from fastapi import APIRouter

from app.tags import USERS_TAG

router = APIRouter(
    prefix="/users",
    tags=[USERS_TAG],
    dependencies=[]
)


@router.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
