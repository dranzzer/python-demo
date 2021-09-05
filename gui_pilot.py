from tkinter import *
from tkcalendar import *



root = Tk()
root.title('Generator')
root.geometry("600x400")

cal1 = Calendar (root, selectmode = "day", year=2020, month=5, day=22)
cal1.pack(pady=20)


def grab_date():
    label.config(text=cal1.get_date())

button = Button(root,text="get date",command=grab_date)
button.pack(pady=20)

label = Label(root,text="")
label.pack(pady=20)

root.mainloop()