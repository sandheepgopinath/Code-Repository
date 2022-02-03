import sqlite3

conn=sqlite3.connect('test_database.db')
print('Created a database')
cursor=conn.cursor()
print('Dropping any  existing table')
cursor.execute('DROP TABLE IF EXISTS Something')
conn.execute('CREATE TABLE Something (Name varchar(20), Age INT)')
print('Table created')

conn.close()

