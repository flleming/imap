from datetime import date
from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    name: str
    password: str

    class Config:
        orm_mode = True
