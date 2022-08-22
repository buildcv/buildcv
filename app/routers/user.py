from datetime import datetime


from pydantic import BaseModel



class UserBase(BaseModel):
    uid: str
    name: str
    email: str
    birthday: datetime
    class Config:
        orm_mode = True


