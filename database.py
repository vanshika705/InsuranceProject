import sqlite3
# to create database and table
connection = sqlite3.connect("insurance.db")

query = """create table project 
        (age integer, sex integer, bmi integer, 
        children integer, smoker integer, 
        weight integer, region varchar(5),
        prediction varchar(10))"""

# cursor sql
cur = connection.cursor()
cur.execute(query)
print("Your database and table is created!")
cur.close()
connection.close()
