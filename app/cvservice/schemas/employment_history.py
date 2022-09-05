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


