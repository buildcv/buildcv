from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import mapper
from sqlalchemy.sql import select
from schemas.user import User

import pyodbc 
import urllib


server = 'localhost,1433' 
database = 'resume' 
username = 'sa' 
password = 'p3dc68f2Q@#' 
TrustServerCertificate = 'yes'
encrypt = 'yes'

params = urllib.parse.quote_plus(f"DRIVER={'ODBC Driver 18 for SQL Server'};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate={TrustServerCertificate};Encrypt={encrypt}")

# create sql server engine 
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")
# list all tables 
metadata = MetaData()
metadata.reflect(bind=engine)
print(metadata.tables.keys())
