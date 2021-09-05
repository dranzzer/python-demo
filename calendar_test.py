import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

def dateentry_view():
    def print_sel(e):
        print(cal.get_date())

    top = tk.Toplevel(root)

    ttk.Label(top, text='Choose date').pack(padx=10, pady=10)
    cal = DateEntry(top, width=12, background='darkblue',
                foreground='white', borderwidth=2)
    cal.pack(padx=10, pady=10)
    cal.bind("<<DateEntrySelected>>", print_sel)

root = tk.Tk()
ttk.Button(root, text='DateEntry', command=dateentry_view).pack(padx=10, pady=10)
root.mainloop()