import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="",database="sampledb1")
mycursor=mydb.cursor()
# mycursor.execute("drop table tb1")
mycursor.execute("create table tb1 (sno int auto_increment primary key, sname varchar(20) default'-', mno varchar(12) default'-')")
print("created")
mycursor.close()
mydb.close()