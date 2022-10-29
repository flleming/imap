from core.db import engine
from model import request, user


def databaseInt() -> None:
    request.Base.metadata.create_all(bind=engine,)
    user.Base.metadata.create_all(bind=engine)
