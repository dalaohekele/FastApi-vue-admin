from fastapi import APIRouter

router = APIRouter()


@router.post("/login",summary="用户登录认证",)
async def login():
    pass
