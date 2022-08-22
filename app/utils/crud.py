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

    type(base_user.birthday)

    user = User(name=base_user.name, birthday=base_user.birthday, uid=base_user.uid, email=base_user.email)
    print(user)
     # convert pydantic user to sqlalchemy user 
    db = next(get_db())
    db.add(user)
    db.commit()






    return user