from datetime import datetime


from pydantic import BaseModel



class User(BaseModel):
    uid: str
    name: str
    email: str
    birthday: datetime


