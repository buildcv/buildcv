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

from models.user import User

import urllib


server = 'localhost,1433' 
database = 'resume' 
username = 'sa' 
password = 'p3dc68f2Q@#' 
TrustServerCertificate = 'yes'
encrypt = 'yes'
import random

params = urllib.parse.quote_plus(f"DRIVER={'ODBC Driver 18 for SQL Server'};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate={TrustServerCertificate};Encrypt={encrypt}")

# create sql server engine 
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

# create session 
Session = sessionmaker(bind=engine)

session = Session()

user_by_id = session.query(User).filter(User.uid == 'newUID').first()
# print user
print(user_by_id.name)
session.close()