import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="",database="sampledb1")
mycursor=mydb.cursor()
mycursor.execute("show tables")
for i in mycursor:
    print(i,"\n")

mycursor.execute("desc tb1")
for i in mycursor:
    print(i)
mycursor.close()
mydb.close()