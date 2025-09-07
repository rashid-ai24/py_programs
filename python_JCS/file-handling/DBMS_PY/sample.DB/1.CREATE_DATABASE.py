import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="")
mycursor=mydb.cursor()
db=input("Enter the DataBase name: ")
mycursor.execute(f"create database if not exists {db}")
print(f"DataBase created on the name of {db}")
mycursor.execute("show databases")
for i in mycursor:
    print(i)
mydb.close()