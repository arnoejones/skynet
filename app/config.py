import pandas as pd
import app.sqlconnect


df = pd.DataFrame()

class Config(object):

    radio_query = []

    if len(radio_query) > 0:
        df = app.sqlconnect.getData(radio_query[-1])
    else:
        radio_query = ["SELECT count(DISTINCT LogTimeStamp) AS 'Total Log Entries' FROM EgmStatus"]
        df = app.sqlconnect.getData(radio_query[-1])

    column_names_list = list(df.columns.values)
    column_names_count = len(column_names_list)

    csv_table = ''
