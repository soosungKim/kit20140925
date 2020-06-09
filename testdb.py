import sqlite3
conn = sqlite3.connect('mydb.db')

c = conn.cursor()
c.execute("CREATE TABLE student(num varchar(50), name varchar(50))")
conn.commit()
conn.close