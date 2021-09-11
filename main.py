import sys
import csv
import pypyodbc as odbc
from tkinter import *
from tkinter import messagebox
from tkcalendar import *
from datetime import *

# DB connection!
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
    global string_start_date
    string_start_date = "2020-01-01"
    global string_end_date
    string_end_date = "2021-08-29"


    def range_update(e):
        format = "%m/%d/%y"

        string_start_date = datetime.strptime(cal1.get_date(), format).strftime("%Y-%m-%d")
        string_end_date = datetime.strptime(cal2.get_date(), format).strftime("%Y-%m-%d")

        if cal1.get_date() > cal2.get_date():
            global user_date_output
            user_date_output = "Warning! Starting Date Cannot be after Ending Date!"
            messagebox.showwarning('ERROR',
                                   'Start Date cannot be after End Date! Report will not generate with incorrect parameters!')
        else:
            user_date_output = "Your current report will be generated from " + string_start_date + " to " + string_end_date

        label.config(text=user_date_output)


    def report_generator():
        format = "%m/%d/%y"
        string_start_date = datetime.strptime(cal1.get_date(), format).strftime("%Y-%m-%d")
        string_end_date = datetime.strptime(cal2.get_date(), format).strftime("%Y-%m-%d")

        if cal1.get_date() > cal2.get_date():
            messagebox.showwarning('ERROR', 'Start Date cannot be after End Date! Report is not generated :(')

        else:
            cursor = conn.cursor()
            sql = "SELECT * FROM dbo.covid_deaths2 WHERE date >= '" + string_start_date + "' AND date <='" + string_end_date + "' ORDER BY location,date"

            # executing SQL

            cursor.execute(sql)

            # get result
            res = cursor.fetchall()
            with open("report_" + string_start_date + "_to_" + string_end_date + ".csv", "w", newline="") as file:
                csv.writer(file).writerow(x[0] for x in cursor.description)
                for row in res:
                    csv.writer(file).writerow(row)

            print("Report Generated! :D")
            # cursor close
            cursor.close()
            messagebox.showinfo('SUCCESS', 'Report has been generated! Please check root directory!!')


    window = Tk()
    window.title('Generator')
    window.geometry("800x300")

cal1 = Calendar(window, selectmode="day", year=2020, month=1, day=1, mindate=date(2020, 1, 1),
                maxdate=date(2021, 8, 29))
cal2 = Calendar(window, selectmode="day", year=2021, month=8, day=29, mindate=date(2020, 1, 1),
                maxdate=date(2021, 8, 29))
cal1.grid(row=1, column=0,columnspan = 3)
cal2.grid(row=1, column=5,columnspan = 3)
cal1.bind("<<CalendarSelected>>", range_update)
cal2.bind("<<CalendarSelected>>", range_update)

button = Button(window, text="Generate Report", command=report_generator)
button.grid(row=4, column=1)



#labels
label = Label(window, text="Your current report will be generated from 2020-01-01 to 2020-08-29")
label.grid(row=2, column=0, columnspan=7)
Label(window, text="Start Date :").grid(row=0, column=0)
Label(window, text="End Date :").grid(row=0, column=4)
#Label(windor,text="spacer").grid(row=1,column=)


continent_main_button =StringVar()


#Radio Buttons

continent_button1 = Radiobutton(window, text = 'World', variable = continent_main_button,value="WORLD",command=lambda:print(continent_main_button.get()))
continent_button2 = Radiobutton(window, text = 'Africa', variable = continent_main_button,value="AFRICA",command=lambda:print(continent_main_button.get()))
continent_button3 = Radiobutton(window, text = 'Asia', variable = continent_main_button,value="ASIA",command=lambda:print(continent_main_button.get()))
continent_button4 = Radiobutton(window, text = 'Europe', variable = continent_main_button,value="EUROPE",command=lambda:print(continent_main_button.get()))
continent_button5 = Radiobutton(window, text = 'North America', variable = continent_main_button,value="NORTH AMERICA",command=lambda:print(continent_main_button.get()))
continent_button6 = Radiobutton(window, text = 'Oceania', variable = continent_main_button,value="OCEANIA",command=lambda:print(continent_main_button.get()))
continent_button7 = Radiobutton(window, text = 'South America', variable = continent_main_button,value="SOUTH AMERICA",command=lambda:print(continent_main_button.get()))

continent_button1.grid(column=0,row=3)
continent_button2.grid(column=1,row=3)
continent_button3.grid(column=2,row=3)
continent_button4.grid(column=3,row=3)
continent_button5.grid(column=4,row=3)
continent_button6.grid(column=5,row=3)
continent_button7.grid(column=6,row=3)
continent_button1.select()
print("Current value is "+continent_main_button.get())

window.resizable(False, False)
window.mainloop()


#stable version