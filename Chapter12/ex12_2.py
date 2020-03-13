#Button Code
from tkinter import *
win=Tk()
win.geometry("100x100+100+100")

def click():
    btn["text"]="Button Click"
    print("Button Click")

btn=Button(win,text="click",bg="red",fg="white",font=("Arial",14), command=click)
btn.pack()

win.mainloop()
