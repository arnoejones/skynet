import pandas as pd
import app.sqlconnect


df = pd.DataFrame()

class Config(object):

    radio_query = [
        "select top 5 count(GameName) as 'Game Name Count with G2S Enabled', GameName as 'Game Name Enabled' from GameLogs where GameName <> '' and G2S like '%G2STrue%' Group by GameName Order By 'Game Name Count with G2S Enabled' DESC"]

    df = app.sqlconnect.getData(radio_query[-1])

    column_names_list = list(df.columns.values)
    column_names_count = len(column_names_list)
    radio_query = []
    csv_table = ''
