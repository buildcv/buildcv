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


from schemas.user import User

import pyodbc 
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


metadata = MetaData()

# insert into users 
users = Table('users', metadata, autoload=True, autoload_with=engine)
connection = engine.connect()


insert_stmt = users.insert().values(birthday=datetime.datetime.now(), name='abdullah',email='a77x86@gmail.com',uid='user_id')
result_proxy = connection.execute(insert_stmt)
result_set = result_proxy.fetchall()
