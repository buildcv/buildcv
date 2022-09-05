from datetime import date, datetime, time, timedelta


from pydantic import BaseModel


# create EmploymentReferences model
class EmploymentReferences(BaseModel):
    user_uid: str
    composite_cv_id_reference: str
    reference_full_name : str
    company : str
    reference_phone_number : str
    reference_email : str
