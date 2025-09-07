import sqlite3

con=sqlite3.connect("testdb.db")

cur=con.cursor()

# sql="create table if not exists testTb (id integer primary key autoincrement, name varchar(15) not null, email varchar(25) unique)"

# cur.execute(sql)
# con.commit()

# sql="insert into testTb(name,email) values(?,?)"
# cur.execute(sql,(''))

con.commit()
cur.close()
con.close()