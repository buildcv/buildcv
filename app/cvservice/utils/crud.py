from http.client import HTTPException
import sys
import os
from unicodedata import name
from data.models import Education, User

from schemas.cv_lookup import CVLookup 
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from schemas.user import UserBase

from database.sqlserver import get_db
from utils import model_schema_convert






def get_all_users():
    db = next(get_db())
    users = db.query(User).all()
    # convert sqlalchemy users to pydantic users and return

    return users




def create_user(base_user: UserBase):

    # check if user uid exists in database
    db = next(get_db())
    user = db.query(User).filter_by(uid=base_user.uid).first()
    if user:
        raise HTTPException(status_code=400, detail="User already exists")
    else:
        # create new user
        user = User(name=base_user.name, registration_date=base_user.registration_date, uid=base_user.uid, email=base_user.email)
        # save user to database
        db.add(user)
        db.commit()
        db.close()
        return user




def get_lookup_by_uid(uid):
    db = next(get_db())
    lookup = db.query(CVLookup).filter(CVLookup.user_uid == uid).first()
    db.close()
    return lookup




def create_education_entry(education: Education):

    # convert education schema to education model
    education_model = model_schema_convert.education_schema_to_model(education)
    # insert education model into database
    db = next(get_db())
    db.add(education_model)
    db.commit()
    db.close()    
    return education 



def update_education_entry(education: Education):

    # convert education schema to education model
    education_model = model_schema_convert.education_schema_to_model(education)
    # update education model into database
    db = next(get_db())
    result = db.query(Education).filter(Education.composite_cv_id_reference == education.composite_cv_id_reference)
    # print the query result 
    print(result)

    return education_model