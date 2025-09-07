import sqlite3, json

con=sqlite3.connect('testdb.db')
cur=con.cursor()

rows=[]
cur.execute('select * from testTb')
rows=cur.fetchall()

cols=[col[0] for col in cur.description]

json_file=[dict(zip(cols,row)) for row in rows]

with open('json.tb.json', 'w',encoding='utf-8') as f:
    json.dump(json_file,f, indent=4, ensure_ascii=False)