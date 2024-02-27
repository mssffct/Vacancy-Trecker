from typing import Union

from fastapi import APIRouter

from app.tags import JOBS_TAG

router = APIRouter(
    prefix="/jobs",
    tags=[JOBS_TAG],
    dependencies=[]
)


@router.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
