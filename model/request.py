from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.types import Date
from core.db import Base


class Request(Base):
    __tablename__ = "Request"

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String(255))
    location = Column(String(255))
    companyName = Column(String(255))
    companyLocation = Column(String(255))
    createdDate = Column(Date)
    requestDate = Column(Date)
    title = Column(String(255))
    url = Column(Text())

