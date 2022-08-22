from datetime import date, datetime, time, timedelta


from pydantic import BaseModel



class UserBase(BaseModel):
    id: int
    uid: str
    name: str
    email: str
    birthday: date
    class Config:
        orm_mode = True


