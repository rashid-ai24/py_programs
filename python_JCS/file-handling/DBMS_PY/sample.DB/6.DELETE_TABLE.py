import mysql.connector
db=input("Enter the DataBase name: ")
mydb=mysql.connector.connect(host="localhost",user="root",password="",database=f"{db}")
mycursor=mydb.cursor()
mycursor.execute("drop table json_exp")
mydb.commit()
mycursor.close()
mydb.close()