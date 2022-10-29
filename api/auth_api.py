from datetime import timedelta
import jwt
import datetime as dt
from fastapi import APIRouter, HTTPException
from starlette import status

from core.config import ACCESS_TOKEN_EXPIRES, SECRET_KEY, ALGORITHM
from serialize.token import Token

router = APIRouter()


async def auth(token: str) -> bool:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        sub: str = payload.get("sub")
        if sub is None or sub != "valid token":
            raise credentials_exception
        return True
    except jwt.PyJWTError:
        raise credentials_exception


def create_access_token(expires_delta: dt.timedelta = None):
    now = dt.datetime.utcnow()
    if expires_delta:
        expire = now + expires_delta
    else:
        expire = now + dt.timedelta(minutes=15)
    to_encode = {
        'exp': expire,
        'iat': now,
        'sub': "valid token",
    }
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt



