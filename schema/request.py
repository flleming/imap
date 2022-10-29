from datetime import date
from pydantic import BaseModel


class RequestSchema(BaseModel):
    id: int
    subject: str
    location: str
    companyName: str
    companyLocation: str
    createdDate: date
    requestDate: date
    title: str
    url: str

    class Config:
        orm_mode = True
