
import sys
import os 
import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.sqlserver import engine




def check_sql_server_connection():
    db = engine.connect()
    db.execute("SELECT 1")
    db.close()
    print("SQL Server connection successful")

check_sql_server_connection()




