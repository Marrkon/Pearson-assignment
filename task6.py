### Task 6 - Save datasets to DB tables

import pandas as pd 
import sqlite3

# Read csv from the path directory, create sqlite db tables and insert csv inside
def insert_csv_into_db(path):
    # Read csv files
    df_avg_score = pd.read_csv(path + 'test_average_scores.csv')
    df_test_util = pd.read_csv(path + 'test_utilization.csv')

    # Drop redundant idx column
    df_avg_score = df_avg_score.loc[:, df_avg_score.columns != 'Unnamed: 0']
    df_test_util = df_test_util.loc[:, df_test_util.columns != 'Unnamed: 0']

    # Take column names 
    columns_avg = str(tuple(df_avg_score.columns.values))
    columns_util = str(tuple(df_test_util.columns.values))

    # Make database connection
    con = sqlite3.connect(":memory:") # change to 'sqlite:///your_filename.db'
    cur = con.cursor()

    # Create dedicated tables - each for one csv.
    cur.execute("CREATE TABLE avg_score " + columns_avg + ";") 
    cur.execute("CREATE TABLE utils " + columns_util + ";") 

    # Insert data into sqlite database
    df_avg_score.to_sql('avg_score', con, if_exists='append', index=False)
    df_test_util.to_sql('utils', con, if_exists='append', index=False)

    # See db result - unconment below 2 lines 
    print("Tables utils and avg_score: \n")
    print(pd.read_sql_query("SELECT * FROM avg_score", con))
    print(pd.read_sql_query("SELECT * FROM utils", con))

if __name__ == '__main__':
    path = 'datasets/'
    insert_csv_into_db(path)
