import sys
import csv
import pypyodbc as odbc

DRIVER = 'SQL Server'
SERVER_NAME = 'DESKTOP-PGGF8L4'
DATABASE_NAME = 'covid'


conn_string = f"""
	Driver={{{DRIVER}}};
	Server={SERVER_NAME};
	Database={DATABASE_NAME};
	Trust_Connection=yes;
"""

try:
	conn = odbc.connect(conn_string)
	print('we are here')
except Exception as e:
	print(e)
	print('task is terminated')
	sys.exit()
else:
	cursor = conn.cursor()
	sql = "SELECT * FROM covid_deaths$"

	#executing SQL

	cursor.execute(sql)

	#get result
	res = cursor.fetchall()
	with open ("new_filve.csv","w") as file:
		for row in res:
			csv.writer(file).writerow(row)

	

	print("done")
	#cursor close
	cursor.close()		