from datetime import date, datetime, time, timedelta


from pydantic import BaseModel

# create cv lookup model 
class CVLookup(BaseModel):
    user_uid: str
    composite_cv_id: str
    users: str
    cvlookups: str
