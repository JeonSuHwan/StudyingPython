#login
from tkinter import *
win=Tk()

def Login():
    print("ID :",eid.get())
    print("PW :",epw.get())
    if var.get()==1:
        print("You are ADMIN")
    else:
        print("You are USER")

def Cancel():
    print("Cancel")
    admin.deselect()

#ID
lid=Label(win,text="ID")
lid.pack()
eid=Entry(win)
eid.pack()

#Password
lpw=Label(win,text="PW")
lpw.pack()
epw=Entry(win,show='*')
epw.pack()

#User or Admin
var=IntVar()
admin=Checkbutton(win,text="Admin",variable=var)
admin.pack(side=LEFT)

#Buttons
login=Button(win,text="Login",command=Login)
login.pack(side=LEFT)
cancel=Button(win,text="Cancel",command=Cancel)
cancel.pack(side=RIGHT)

win.mainloop()
