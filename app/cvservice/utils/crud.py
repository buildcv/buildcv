from http.client import HTTPException
import sys
import os
from unicodedata import name 
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.user import User
from schemas.user import UserBase

from database.sqlserver import get_db



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
        user = User(name=base_user.name, birthday=base_user.birthday, uid=base_user.uid, email=base_user.email)
        # save user to database
        db.add(user)
        db.commit()
        db.close()
        return user

