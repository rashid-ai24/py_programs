import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="",database="sampledb1")
mycursor=mydb.cursor()
sql = "insert into tb1() values ()"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "rows affected.")
mycursor.close()
mydb.close()