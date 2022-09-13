from datetime import date, datetime, time, timedelta


from pydantic import BaseModel

# create EmploymentHistory model 
class EmploymentHistory(BaseModel):
    user_uid: str
    composite_cv_id_reference: str
    job_title: str
    employer: str
    start_date: date
    end_date: date
    city: str


class EmploymentHistory_job_title(BaseModel):
    cv_id: str
    job_title: str

class EmploymentHistory_employer(BaseModel):
    cv_id: str
    employer: str


class EmploymentHistory_start_date(BaseModel):
    cv_id: str
    start_date: date


class EmploymentHistory_end_date(BaseModel):
    cv_id: str
    end_date: date

class EmploymentHistory_city(BaseModel):
    cv_id: str
    city: str

 
class EmploymentHistoryDel(BaseModel):
    cv_id: str

    class Config:
        orm_mode = True



