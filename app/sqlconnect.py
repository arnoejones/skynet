import pandas.io.sql as psql
from sqlalchemy import create_engine

# Skynet production db
# Query the SQL Server database and put the results into a Pandas dataframe. This will
# allow easier manipulation and graphics displays.

def getData(query):
    # ServerName = 'rnop-ctpa02'
    # Database = 'FTA'
    # Driver = "driver=SQL Server Native Client 11.0"
    #ServerName = 'Godzilla\ArnoSqlServer'
    ServerName = 'USNVR-W1005006\SKYNETLOCAL'
    Database = 'FTA'
    Driver = "driver=SQL Server Native Client 11.0"

    engine = create_engine('mssql+pyodbc://' + ServerName + '/' + Database + "?" + Driver)

    print("THE QUERY TO SQLCONNECT IS {}".format(query))
    if query is None:
        query = "SELECT count(DISTINCT LogTimeStamp) AS 'Total Log Entries' FROM EgmStatus"

    df = psql.read_sql(query, engine)
    fill_qd(query)
    return df


qd = ['']

def fill_qd(z):
    qd[0] = z
    print('**** qd: ', qd)

def query_desc():
    return qd

qraw = ['']

def fill_qraw(z):
    qraw[0] = z
    print('**** qraw: ', qraw)

def query_raw():
    return qraw
