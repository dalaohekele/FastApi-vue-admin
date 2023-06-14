from fastapi import APIRouter
from api.system.user_api import router as user_router

api_router = APIRouter()

api_router.include_router(user_router, prefix='/user', tags=["用户"])

__all__ = ["api_router"]
