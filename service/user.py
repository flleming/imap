from sqlalchemy.orm import Session
from sqlalchemy import insert
from fastapi import Depends

from core.db import getDb
from core.config import PWD_CONTEXT
from model.user import User


class UserService:
    session: Session

    def __init__(self, db: Session = Depends(getDb)):
        self.session = db

    async def createUser(self, **args: User):
        stmt = insert(User).values(args)
        result = self.session.execute(stmt)
        print(result)
        self.session.commit()

    async def get_by_email(self,name):
        return self.session.query(User).filter(User.name==name).first()
    def check_password(self, password: str,passwordToCheck):
        if passwordToCheck:
            return PWD_CONTEXT.verify(password, passwordToCheck)
    def hashPassword(self,password:str):
        return PWD_CONTEXT.hash(password)

