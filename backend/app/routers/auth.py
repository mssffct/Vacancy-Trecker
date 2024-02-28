from fastapi import APIRouter

from app.tags import AUTH_TAG

router = APIRouter(
    prefix="/auth",
    tags=[AUTH_TAG],
    dependencies=[]
)


@router.post("/token/login")
async def login(user: dict):
    return {"user": user}

@router.delete("/token/logout")
async def logout(user: dict):
    return {"user": user}