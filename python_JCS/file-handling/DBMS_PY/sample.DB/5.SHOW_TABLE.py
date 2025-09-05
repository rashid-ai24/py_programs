import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="",database="sampledb1")
mycursor=mydb.cursor()
mycursor.execute("select * from tb1")
rows = mycursor.fetchall()
print("Tables data: \n")
for row in rows:
    print(row)
mycursor.close()
mydb.close()