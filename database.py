import sqlite3
# to create database and table
connection = sqlite3.connect("insurance.db")

query = """create table project 
        (age integer, sex varchar(5), bmi integer, 
        children integer, smoker varchar(5), 
        weight varchar(5), region varchar(5),
        prediction varchar(10))"""

query_to_fetch = """ select * from project """

# cursor sql is a temporary memory
cur = connection.cursor()
# cur.execute(query)
# print("Your database and table is created!")

#  to fetch data form database 
cur.execute(query_to_fetch)
for record in cur.fetchall():
        print(record)

cur.close()
connection.close()

# Assignment smoker --> yes or no  , gender ---> female or male , health ---> 4 types 