#PhotoImage Code
from tkinter import *
win=Tk()

photo1=PhotoImage(file='balloon.png')
photo2=PhotoImage(file='balloon2.png')

def click():
    lbl["image"]=photo2
    
lbl=Label(win,image=photo1)
lbl.pack(fill=BOTH)

btn=Button(win,text='click',command=click)
btn.pack()

win=mainloop()
