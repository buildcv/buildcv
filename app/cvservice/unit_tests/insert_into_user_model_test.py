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

from models.user import User







user = User(name='Abdullah', birthday=datetime.datetime.now(), uid='hasan',email='Abdullah@gmail.com')


# save user to database
session = next(get_db())
session.add(user)
session.commit()
session.close()