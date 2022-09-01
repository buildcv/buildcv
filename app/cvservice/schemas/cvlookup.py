from datetime import date, datetime, time, timedelta


from pydantic import BaseModel


class CvLookupBase(BaseModel):
    user_uid: str
    composite_cv_id: str
    class Config:
        orm_mode = True

