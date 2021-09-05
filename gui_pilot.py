from tkinter import *
from tkcalendar import *
from datetime import date
#DB connection!
DRIVER = 'SQL Server'
SERVER_NAME = 'DESKTOP-PGGF8L4'
DATABASE_NAME = 'covid'

conn_string = f"""
	Driver={{{DRIVER}}};
	Server={SERVER_NAME};
	Database={DATABASE_NAME};
	Trust_Connection=yes;
"""



window = Tk()
window.title('Generator')
window.geometry("557x400")
def range_update(e):
    start_date_ui = cal1.get_date()
    end_date_ui = cal2.get_date()
    user_date_output = "Your current report will be generated from " + start_date_ui + " to " + end_date_ui
    label.config(text=user_date_output)


def grab_date():

    start_date_ui = cal1.get_date()
    end_date_ui = cal2.get_date()
    user_date_output = "Your current report will be generated from "+ start_date_ui +" to " + end_date_ui
    label.config(text=user_date_output)



cal1 = Calendar(window, selectmode = "day", year=2020, month=1, day=1,mindate=date(2020,1,1),maxdate=date(2021,8,29))
cal2 = Calendar(window, selectmode = "day", year=2021, month=8, day=29,mindate=date(2020,1,1),maxdate=date(2021,8,29))
cal1.grid(row=1,column=0)
cal2.grid(row=1,column=2)
cal1.bind("<<CalendarSelected>>", range_update)
cal2.bind("<<CalendarSelected>>", range_update)






button = Button(window,text="get date",command=grab_date)
button.grid(row=4,column=1)

label = Label(window,text="Your current report will be generated from 2020-01-01 to 2020-08-29")
label.grid(row=3,column=0,columnspan=3)
Label(window,text="Start Date :").grid(row=0,column=0)
Label(window,text="Start Date :").grid(row=0,column=2)




window.resizable(False,False)
window.mainloop()