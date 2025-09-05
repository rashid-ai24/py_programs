import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="",database="sampledb1")
mycursor=mydb.cursor()
mycursor.execute("truncate table tb1")
mydb.commit()
mycursor.close()
mydb.close()