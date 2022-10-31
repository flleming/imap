from core.constant import USER_NAME, USER_PASSWORD
from core.db import engine,getDb
from model import request, user
from sqlalchemy import insert
from core.config import PWD_CONTEXT

def databaseInt() -> None:
    request.Base.metadata.create_all(bind=engine,)
    user.Base.metadata.create_all(bind=engine)

async def InitUser():
    if engine.dialect.has_table(engine.connect(),user.User.__tablename__):
        session=next(getDb())
        if session.query(user.User).first() is None:
            stmt = insert(user.User).values({"name":USER_NAME,"password":PWD_CONTEXT.hash(USER_PASSWORD)})
            result = session.execute(stmt)
            print(result)
            session.commit()