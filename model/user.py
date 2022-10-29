from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date
from core.db import Base


class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(225))
    password = Column(String(225))


