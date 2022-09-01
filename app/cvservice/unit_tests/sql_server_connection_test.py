from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import mapper
from sqlalchemy.sql import select
import sys
import os 
import datetime
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.sqlserver import engine



# check sql server connection 
def check_sql_server_connection():
    db = engine.connect()
    db.execute("SELECT 1")
    db.close()
    print("SQL Server connection successful")

check_sql_server_connection()


# list all tables from sql server
def list_all_tables():
    metadata = MetaData()
    metadata.reflect(engine)
    print(metadata.tables.keys())


list_all_tables()


