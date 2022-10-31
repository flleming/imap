from fastapi import APIRouter
from .auth_api import router as auth_router
from .user_api import router as user_router
from .request_api import router as request_router
router = APIRouter()
router.include_router(router=auth_router, tags=['auth'])
router.include_router(router=user_router)
router.include_router(router=request_router)
