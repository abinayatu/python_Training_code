"""
Get data from
1) database
2) db_data.json
3) log_report.txt

and produce one single report
and write to below files

pandas_report.csv
pandas_report.xlsx
pandas_report.json
pandas_report.xml
"""

print("Get data from database")
print("-"*20)
# --------------

print("Creating database 'my_database.sqlite3'")
# my_db_connection = sqlite3.connect(r'C:\python_training\programs\my_database.sqlite3')
print("Done\n")


import sqlite3
my_db_connection = sqlite3.connect('my_database.sqlite3')
print("Creating cursor object ")
my_db_cursor = my_db_connection.cursor()
print("Done\n")
import pandas as pd
my_db_df = pd.read_sql("SELECT * FROM MY_TABLE", my_db_connection)

print(my_db_df)

print("#"*40, end="\n\n")
################################

print("Get data from json")
print("-"*20)
# --------------

my_json_df = pd.read_json("db_data.json")
print(my_json_df)

print("#"*40, end="\n\n")
################################

print("Get data from text file")
print("-"*20)
# --------------

my_text_df = pd.read_csv("log_report.txt", sep="\t")
print(my_text_df)

print("#"*40, end="\n\n")




################################


#### 2 nd ####

"""
Get data from
1) database
2) db_data.json
3) log_report.txt

and produce one single report
and write to below files

pandas_report.csv
pandas_report.xlsx
pandas_report.json
pandas_report.xml
"""

print("Get data from database")
print("-"*20)
# --------------

import sqlite3
my_db_connection = sqlite3.connect('my_database.sqlite3')

import pandas as pd
my_db_df = pd.read_sql("SELECT * FROM MY_TABLE", my_db_connection)

print(my_db_df)

print("#"*40, end="\n\n")
################################

print("Get data from json")
print("-"*20)
# --------------

my_json_df = pd.read_json("db_data.json")
print(my_json_df)

print("#"*40, end="\n\n")
################################

print("Get data from text file")
print("-"*20)
# --------------

my_text_df = pd.read_csv("log_report.txt", sep="\t")
print(my_text_df)

print("#"*40, end="\n\n")
################################