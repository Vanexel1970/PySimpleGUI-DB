import sqlite3

conn = sqlite3.connect('trading.db')
query = (''' CREATE TABLE portofolio
            (id           integer NOT NULL primary key AUTOINCREMENT, 
            ticker        text NOT NULL);''')
conn.execute(query)
conn.close()