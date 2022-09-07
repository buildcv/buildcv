import email
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.sql import select
import sys
import os 
import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import insert
import urllib


sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Server info 
server = 'sqlserver,1433' 
database = 'resume' 
username = 'sa' 
password = 'p3dc68f2Q@#' 
TrustServerCertificate = 'yes'
encrypt = 'yes'

params = urllib.parse.quote_plus(f"DRIVER={'ODBC Driver 18 for SQL Server'};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate={TrustServerCertificate};Encrypt={encrypt}")

engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")



# db url as string 


# create session 
Session = sessionmaker(bind=engine)

session = Session()

def get_db():
    Session = sessionmaker(bind=engine)
    session = Session()
    try :
        yield session
    finally:
        session.close()
