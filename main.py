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

try:
    conn = odbc.connect(conn_string)
    print('connected to db succesfully')
except Exception as e:
    print(e)
    print('task is terminated')
    sys.exit()
else:

    class FirstApp(Ui_MainWindow):
        def __init__(self, window):
            self.setupUi(window)
            self.button1.clicked.connect(self.generate_report)


            self.startdate.clicked.connect(self.startdatefunc)
            self.startdate.setMinimumDate(QDate(2020,1,1))
            self.startdate.setMaximumDate(QDate(2021, 8, 29))
            self.startdate.setSelectedDate(QDate(2020, 1, 1))



            self.enddate.clicked.connect(self.enddatefunc)
            self.enddate.setMinimumDate(QDate(2020, 1, 1))
            self.enddate.setMaximumDate(QDate(2021, 8, 29))
            self.enddate.setSelectedDate(QDate(2021, 8, 29))

            global start_date_range
            start_date_range = "2020-01-01"
            global end_date_range
            end_date_range = "2021-08-29"





        def startdatefunc(self, qDate):

            global start_date_range
            start_date_range = '{0}-{1}-{2}'.format(qDate.year(), qDate.month(), qDate.day())

        def enddatefunc(self, qDate):
            global end_date_range
            end_date_range = '{0}-{1}-{2}'.format(qDate.year(), qDate.month(), qDate.day())




        def generate_report(self):
            cursor = conn.cursor()

            if datetime.strptime(start_date_range, '%Y-%m-%d') <= datetime.strptime(end_date_range,'%Y-%m-%d'):

                sql = "SELECT * FROM dbo.covid_deaths2 WHERE date >= '" + start_date_range + "' AND date <='" + end_date_range + "' ORDER BY location,date"


                # executing SQL

                cursor.execute(sql)

                # get result
                res = cursor.fetchall()
                with open("report_"+start_date_range+"_to_"+end_date_range+".csv", "w", newline="") as file:
                    csv.writer(file).writerow(x[0] for x in cursor.description)
                    for row in res:
                        csv.writer(file).writerow(row)

                print("Report Generated! :D")
                # cursor close
                cursor.close()
            else:
                print("Please check date range - End Date cannot be before the start!")
                print("Report not generated :(")
                cursor.close()


    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    # create instance of app
    ui = FirstApp(MainWindow)

    # window and start app
    MainWindow.show()
    app.exec_()





