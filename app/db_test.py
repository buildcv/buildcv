import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = '127.0.0.1' 
database = 'resume' 
username = 'sa' 
password = 'p3dc68f2Q@#' 
conn = pyodbc.connect( 
    driver='{ODBC Driver 18 for SQL Server}', 
    server='localhost,1433', 
    database='resume', 
    uid='sa', 
    pwd='p3dc68f2Q@#', 
    encrypt='yes', 
    TrustServerCertificate ='yes',
   
    
    ) 
cursor = conn.cursor()
# list all tables from the database SQL server
cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES")
for row in cursor.fetchall():
    print(row)
