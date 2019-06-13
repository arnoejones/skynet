import pandas.io.sql as psql
from sqlalchemy import create_engine


# Skynet production db
# Query the SQL Server database and put the results into a Pandas dataframe. This will
# allow easier manipulation and graphics displays.
def getData(query):
    ServerName = 'rnop-ctpa02'
    Database = 'FTA'
    Driver = "driver=SQL Server Native Client 11.0"

    engine = create_engine('mssql+pyodbc://' + ServerName + '/' + Database + "?" + Driver)
    if query is not None:
        print("THE QUERY TO SQLCONNECT IS {}".format(query))

        df = psql.read_sql(query, engine)

        return df
    else:  # upon initialization, app won't load because there aren't any default values.  This is for init only.
        print("THE QUERY TO SQLCONNECT IS {}".format(query))
        query = "select top 5 count(GameName) as 'Game Name Count with G2S Enabled', GameName as 'Game Name Enabled' from GameLogs where GameName <> '' and G2S like '%G2STrue%' Group by GameName Order By 'Game Name Count with G2S Enabled' DESC"
        df = psql.read_sql(query, engine)

        return df
