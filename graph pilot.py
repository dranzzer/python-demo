import sys
import csv
import pypyodbc as odbc
from ui import *
from PyQt5.QtCore import QDate
from datetime import datetime


DRIVER = 'SQL Server'
SERVER_NAME = 'DESKTOP-PGGF8L4'
DATABASE_NAME = 'covid'

conn_string = f"""
	Driver={{{DRIVER}}};
	Server={SERVER_NAME};
	Database={DATABASE_NAME};
	Trust_Connection=yes;
"""
global start_date_range
start_date_range = 2020-01-01
try:
    conn = odbc.connect(conn_string)
    print('connected to db succesfully')
except Exception as e:
    print(e)
    print('task is terminated')
    sys.exit()
else:
    cursor = conn.cursor()
    sql = "SELECT * FROM dbo.covid_deaths2 WHERE date >= '" + start_date_range + "' AND date <='" + end_date_range + "' ORDER BY location,date"

    # executing SQL

    cursor.execute(sql)

    # get result
    res = cursor.fetchall()
    with open("report_" + start_date_range + "_to_" + end_date_range + ".csv", "w", newline="") as file:
        csv.writer(file).writerow(x[0] for x in cursor.description)
        for row in res:
            csv.writer(file).writerow(row)

    print("Report Generated! :D")
    # cursor close
    cursor.close()