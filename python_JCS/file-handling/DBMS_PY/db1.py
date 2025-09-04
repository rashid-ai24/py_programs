import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists sampledb1")
print("created")
mycursor.execute("show databases")
for i in mycursor:
    print(i)
