import mysql.connector

db = mysql.connector.connect(host = "127.0.0.1", user = "root", passwd = "hehe")

cursor = db.cursor()


#insert sql query
cursor.execute("show databases")

for i in cursor:
	print(i)