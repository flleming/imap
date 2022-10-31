from datetime import timedelta
import jwt
import datetime as dt
from fastapi import APIRouter, HTTPException, Depends
from starlette import status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from core.config import ACCESS_TOKEN_EXPIRES, SECRET_KEY, ALGORITHM
from model.user import User
from serialize.token import Token
from service.user import UserService

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/token')


# async def auth(token: str) -> bool:
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         sub: str = payload.get("sub")
#         if sub is None or sub != "valid token":
#             raise credentials_exception
#         return True
#     except jwt.PyJWTError:
#         raise credentials_exception
async def auth(token: str = Depends(oauth2_scheme)) -> bool:
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


@router.post('/token', response_model=Token)
async def get_token_api(form_data: OAuth2PasswordRequestForm = Depends(),userService=Depends(UserService)):
    user:User = await userService.get_by_email(form_data.username)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    if not userService.check_password(form_data.password, user.password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token(expires_delta=timedelta(hours=ACCESS_TOKEN_EXPIRES))
    return {"access_token": access_token, "token_type": "bearer"}


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



