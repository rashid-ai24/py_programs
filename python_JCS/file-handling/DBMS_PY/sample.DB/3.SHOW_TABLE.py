import mysql.connector
db=input("Enter the DataBase name: ")
mydb=mysql.connector.connect(host="localhost",user="root",password="",ddatabase=f"{db}")
mycursor=mydb.cursor()
mycursor.execute("show tables")
for i in mycursor:
    print(i,"\n")

mycursor.execute("desc json_exp")
for i in mycursor:
    print(i)
mycursor.close()
mydb.close()