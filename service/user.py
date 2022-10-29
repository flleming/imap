from sqlalchemy.orm import Session
from sqlalchemy import insert
from fastapi import Depends

from core.db import getDb
from model.user import User


class UserService:
    session: Session

    def __init__(self, db: Session = Depends(getDb)):
        self.session = db

    def createUser(self, **args: User):
        stmt = insert(User).values(args)
        result = self.session.execute(stmt)
        print(result)
        self.session.commit()
