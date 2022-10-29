from fastapi import APIRouter, Depends
from .auth_api import create_access_token
from schema.user import UserSchema
import datetime as dt
from core.config import ACCESS_TOKEN_EXPIRES

from service.user import UserService
from model.user import User

router = APIRouter()


@router.get('/token')
async def generate_token():
    return create_access_token(expires_delta=dt.timedelta(hours=ACCESS_TOKEN_EXPIRES))
