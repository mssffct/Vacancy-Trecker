from typing import Union

from fastapi import APIRouter

from app.tags import USERS_TAG

router = APIRouter(
    prefix="/users",
    tags=[USERS_TAG],
    dependencies=[]
)


@router.get("/me")
async def read_me():
    return {"message": "Hello World"}

@router.get("/{user_id}")
async def read_user(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@router.post("/")
async def create_user(user: dict):
    return {"user": user}

@router.patch("/{user_id}")
async def patch_user(user: dict):
    return {"user": user}