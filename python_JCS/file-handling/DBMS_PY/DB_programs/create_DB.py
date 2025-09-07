import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="")
mycursor=mydb.cursor()
# mycursor.execute("create database if not exists DataBase_Name")
print("DataBase created")
mycursor.execute("show databases")
for i in mycursor:
    print(i)
mydb.close()