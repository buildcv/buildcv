import sys
import os 
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.sqlserver import get_db
from models.user import User

# get all users 

def get_all_users():
    db = next(get_db())
    users = db.query(User).all()

    # print users and return users
    for user in users:
        print(user.name)
        print(user.email)
        print(user.birthday)
        print(user.uid)


    return users
   

get_all_users()