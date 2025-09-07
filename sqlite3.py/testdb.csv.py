import sqlite3, csv

con = sqlite3.connect("testdb.db")
cur = con.cursor()

cur.execute("SELECT * FROM testTb")
rows = cur.fetchall()

with open("testTb.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([d[0] for d in cur.description])  # column headers
    writer.writerows(rows)

con.close()