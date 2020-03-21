#GUI
from tkinter import *
import accountModule

win=Tk()
win.title("Account")
win.geometry("300x300")

f1=Frame(win)
Label(f1,text="Content :").pack(side=LEFT)
Entry(f1).pack(side=RIGHT)
f1.pack()
f2=Frame(win)
Label(f2,text="Price :").pack(side=LEFT)
Entry(f2).pack(side=RIGHT)
f2.pack()

win.mainloop()
