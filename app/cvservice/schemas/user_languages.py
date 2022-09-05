from datetime import date, datetime, time, timedelta


from pydantic import BaseModel


# create UserLanguages model
class UserLanguages(BaseModel):
    user_uid: str 
    composite_cv_id_reference: str
    user_language_label: str
