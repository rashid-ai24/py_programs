import mysql.connector
db=input("Enter the DataBase name: ")
mydb=mysql.connector.connect(host="localhost",user="root",password="",database=f"{db}")
mycursor=mydb.cursor()
sql = "insert into tb1() values ()"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "rows affected.")
mycursor.close()
mydb.close()