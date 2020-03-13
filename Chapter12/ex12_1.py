#Label Code
from tkinter import *
win=Tk()

lbl=Label(win, text="PYTHON", bg="green",fg="white")
lbl["text"]='tkinter'
lbl.pack()

lbl2=Label(win,text="PYTHON",bg="red",font=("Helvetica",16))
lbl2.pack()
win.mainloop() #event looping
