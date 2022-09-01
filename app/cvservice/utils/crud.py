from http.client import HTTPException
import sys
import os
from unicodedata import name
from data.models import User

from schemas.cvlookup import CvLookupBase 
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from schemas.user import UserBase

from database.sqlserver import get_db





def create_cv_lookup(cv_lookup_base:CvLookupBase):
    

    pass


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

