import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully")
cursor=conn.cursor()
cursor.execute('DROP TABLE IF EXISTS review')
conn.execute('CREATE TABLE reviews (review varchar(30),sentiment varchar(10),status varchar(10))')
print ("Table created successfully")
conn.close()
