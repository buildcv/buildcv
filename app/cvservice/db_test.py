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



def extract_shapefile(shapefile_path):
    """
    Extract the data from a shapefile into a pandas dataframe.
    """
    import geopandas as gpd
    import pandas as pd
    # Read the shapefile
    gdf = gpd.read_file(shapefile_path)
    # Extract the geometry
    geometry = gdf.geometry
    # Extract the dataframe
    df = gdf.drop(columns=['geometry'])
    # Create a new dataframe with the geometry and data
    df = pd.concat([geometry, df], axis=1)
    return df
    