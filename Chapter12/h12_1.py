#Map selection
from tkinter import *
win=Tk()
win.geometry("300x320")
win.title("Map")

#Photos
p1=PhotoImage(file="africa.png")
p2=PhotoImage(file="america.png")
p3=PhotoImage(file="asia.png")
p4=PhotoImage(file="europe.png")

title=Label(win,text="MAP",font=("Arial",20))
title.pack()

def click():
    if group.get()==1:
        lbl["image"]=p1
    elif group.get()==2:
        lbl["image"]=p2
    elif group.get()==3:
        lbl["image"]=p3
    else:
        lbl["image"]=p4

f=Frame(win)
group=IntVar()
#four radio buttons
Radiobutton(f,text="Africa",variable=group,value=1,command=click).pack(side=LEFT)
Radiobutton(f,text="America",variable=group,value=2,command=click).pack(side=LEFT)
Radiobutton(f,text="Asia",variable=group,value=3,command=click).pack(side=LEFT)
Radiobutton(f,text="Europe",variable=group,value=4,command=click).pack(side=LEFT)
f.pack()

lbl=Label(win,width=300,height=320,bg="gray")
lbl.pack(fill=BOTH)

win.mainloop()
