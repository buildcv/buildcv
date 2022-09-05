from datetime import date, datetime, time, timedelta


from pydantic import BaseModel


# create Skills model
class Skills(BaseModel):
    user_uid: str
    composite_cv_id_reference: str
    skill_name: str
    
    