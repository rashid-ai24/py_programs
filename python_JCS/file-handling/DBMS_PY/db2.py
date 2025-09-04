import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="",database="db1")
mycursor=mydb.cursor()
mycursor.execute("DROP TABLE IF EXISTS tb1")
mycursor.execute("CREATE TABLE tb1(sno INT PRIMARY KEY, sname VARCHAR(20), mno VARCHAR(12))")
print("created")
'''mycursor.execute("create table tb1(sno int primary key,sname varchar(20),mno varchar(12) )")
print("created")'''
mycursor.close()