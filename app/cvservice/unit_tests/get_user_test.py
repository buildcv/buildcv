import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data.models import User 
from database.sqlserver import get_db
import random 




# search users by name
def search_users_by_name(name):
    db = next(get_db())
    users = db.query(User).filter(User.name.like('%'+name+'%')).all()

    # print users and return users
    for user in users:
        print(user.name)
        print(user.email)
        print(user.registration_date)
        print(user.uid)

    return users



# get_random_user
def get_random_user():
    db = next(get_db())
    # 10 random users 
    users = db.query(User).limit(10).all()
    # random user from users
    random_user = random.choice(users)
    return random_user


# get_n_users_by_uid
def get_n_users_by_id(n):
    db = next(get_db())
    users = db.query(User).limit(n).all()

    # print users and return users
    for user in users:
        print(user.name)
        print(user.email)
        print(user.registration_date)
        print(user.uid)

    return users



# get_users_by_offset_and_limit
def get_users_by_offset_and_limit(offset, limit):
    db = next(get_db())
    users = db.query(User).offset(offset).limit(limit).all()

    # print users and return users
    for user in users:
        print(user.name)
        print(user.email)
        print(user.registration_date)
        print(user.uid)

    return users



# get user by id
def get_user_by_uid(uid):
    db = next(get_db())
    user = db.query(User).filter_by(uid=uid).first()
    return user

# get all users 
def get_all_users():
    db = next(get_db())
    users = db.query(User).all()

    # print users and return users
    for user in users:
        print(user.name)
        print(user.email)
        print(user.registration_date)
        print(user.uid)


    return users
   


def get_n_users(n):
    db = next(get_db())
    users = db.query(User).limit(n).all()

    # print users and return users
    for user in users:
        print(user.name)
        print(user.email)
        print(user.registration_date)
        print(user.uid)

    return users



print(get_random_user().uid)