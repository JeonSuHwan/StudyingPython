#place code
from tkinter import *
win=Tk()
win.geometry("200x200+1100+250")

Button(win,text='0,0').place(x=0,y=0)
Button(win,text='50,50').place(x=50,y=50)
Button(win,text="70,65").place(x=70,y=65)

win.mainloop()
