import mysql.connector
db=input("Enter the DataBase name: ")
mydb=mysql.connector.connect(host="localhost",user="root",password="",database=f"{db}")
mycursor=mydb.cursor()
# mycursor.execute("drop table tb1")
mycursor.execute("create table if not exists tb1 (sno int auto_increment primary key, sname varchar(20) default'-', mno varchar(12) default'-')")
print("created")
mycursor.close()
mydb.close()