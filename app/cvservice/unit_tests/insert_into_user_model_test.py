import email
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import mapper
from sqlalchemy.sql import select
import sys
import os 
import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import insert



sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.sqlserver import get_db

from data.models import CVLookup  , User

from create_random_users import create_random_users , create_user



def insert_into_user_model():
    user = create_user()
    db = next(get_db())
    db.add(user)
    db.commit()
    db.close()
    return user



def insert_users_into_user_model(count):
    users = create_random_users(count)
    db = next(get_db())
    db.add_all(users)
    db.commit()
    db.close()
    return users






# Single user insert test
# insert_into_user_model()


insert_users_into_user_model(100)
