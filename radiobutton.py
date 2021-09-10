from tkinter import *

window=Tk()


window.geometry("400x400")

var =IntVar()
var1 = IntVar()


Radiobutton1 = Radiobutton(window, text = 'test', variable = var,value=1)
Radiobutton2 = Radiobutton(window, text = 'test2', variable = var1,value=2)
Radiobutton3 = Radiobutton(window, text = 'test3', variable = var1,value=3,command=lambda:print(var1.get()))

Radiobutton1.grid(column=0,row=0)
Radiobutton2.grid(column=1,row=0)
Radiobutton3.grid(column=2,row=0)
Radiobutton3.select()
print("Current value is "+str(var1.get()))

window.mainloop()