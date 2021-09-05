from tkinter import *
from tkcalendar import *
from datetime import date



window = Tk()
window.title('Generator')
window.geometry("557x400")

cal1 = Calendar(window, selectmode = "day", year=2020, month=1, day=1,mindate=date(2020,1,1),maxdate=date(2021,8,29))
cal2 = Calendar(window, selectmode = "day", year=2021, month=8, day=29,mindate=date(2020,1,1),maxdate=date(2021,8,29))
cal1.grid(row=1,column=0)
cal2.grid(row=1,column=2)



def grab_date():
    label.config(text=cal1.get_date())

button = Button(window,text="get date",command=grab_date)
button.grid(row=4,column=1)

label = Label(window,text="")
label.grid(row=3,column=1)
Label(window,text="Start Date :").grid(row=0,column=0)
Label(window,text="Start Date :").grid(row=0,column=2)




window.resizable(False,False)
window.mainloop()