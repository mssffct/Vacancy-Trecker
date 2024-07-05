from typing import Union

from fastapi import APIRouter

from tags import RESULTS_TAG

router = APIRouter(
    prefix="/results",
    tags=[RESULTS_TAG],
    dependencies=[]
)


@router.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
