from tkinter import *
from tkcalendar import *



window = Tk()
window.title('Generator')
window.geometry("650x400")

cal1 = Calendar(window, selectmode = "day", year=2020, month=5, day=22)
cal2 = Calendar(window, selectmode = "day", year=2020, month=5, day=22)
cal1.grid(row=1,column=0)
cal2.grid(row=1,column=2)



def grab_date():
    label.config(text=cal1.get_date())

button = Button(window,text="get date",command=grab_date)
button.grid(row=3,column=1)

label = Label(window,text="")
label.grid(row=4,column=2)
Label(window,text="Start Date :").grid(row=0,column=0)
Label(window,text="Start Date :").grid(row=0,column=2)




window.resizable(False,False)
window.mainloop()