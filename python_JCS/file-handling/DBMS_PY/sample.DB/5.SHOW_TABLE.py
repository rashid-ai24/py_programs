import mysql.connector
db=input("Enter the DataBase name: ")
mydb=mysql.connector.connect(host="localhost",user="root",password="",database=f"{db}")
mycursor=mydb.cursor()
mycursor.execute("select * from json_exp")
rows = mycursor.fetchall()
print("Tables data: \n")
for row in rows:
    print(row)
mycursor.close()
mydb.close()