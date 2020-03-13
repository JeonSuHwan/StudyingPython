#greetings
from tkinter import *
win=Tk()
win.geometry("200x200+400+200")

lbl=Label(win,text="",font=("Arial",40))
lbl.pack()

#Korean
def korean():
    lbl["text"]="안녕"
kor=Button(win,bg="yellow",text="한국어",command=korean)
kor.pack(fill=BOTH,expand=YES)

#English
def english():
    lbl["text"]="Hello"
eng=Button(win,bg="green",text="English",command=english)
eng.pack(fill=BOTH,expand=YES)

#Spanish
def spanish():
    lbl["text"]="Hola"
spa=Button(win,bg="pink",text="Spanish",command=spanish)
spa.pack(fill=BOTH,expand=YES)

win.mainloop()
