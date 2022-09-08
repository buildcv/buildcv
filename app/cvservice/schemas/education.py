from datetime import date, datetime, time, timedelta


from pydantic import BaseModel


# create education model 
class EducationSchema(BaseModel):
    composite_cv_id_reference: str
    user_uid: str
    school: str
    degree: str
    description: str
    start_date: date
    end_date: date
    
    
class Education_school(BaseModel):
    cv_id: str
    school: str



class Education_degree(BaseModel):
    cv_id: str
    degree: str

class Education_description(BaseModel):
    cv_id: str
    description: str

class Education_start_date(BaseModel):
    cv_id: str
    start_date: date


class Education_end_date(BaseModel):
    cv_id: str
    end_date: date



class EducationDel(BaseModel):
    cv_id: str

    class Config:
        orm_mode = True

