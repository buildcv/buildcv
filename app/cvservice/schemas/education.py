from datetime import date, datetime, time, timedelta


from pydantic import BaseModel


# create education model 
class Education(BaseModel):
    composite_cv_id_reference: str
    user_uid: str
    school: str
    degree: str
    description: str
    start_date: date
    end_date: date
    
    



