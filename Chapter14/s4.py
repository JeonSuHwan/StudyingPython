#GUI
from tkinter import *
import accountModule as ac

win=Tk()
win.title("Account")
win.geometry("300x300")

def deposit():
    a.deposit(int(pri.get()))
    price=a.numFormat(int(pri.get()))
    msg=con.get()+'    '+price+'    '+a.getBalance()
    lb.insert(END,msg)
    con.delete(0,last=len(con.get()))
    pri.delete(0,last=len(pri.get()))
    lbl["text"]='total:'+str(lb.size()-1)
def withdraw():
    a.withdraw(int(pri.get()))
    price=a.numFormat(int(pri.get()))
    msg=con.get()+'    '+price+'    '+a.getBalance()
    lb.insert(END,msg)
    con.delete(0,last=len(con,get()))
    pri.delete(0,last=len(con.get()))
    lbl["text"]='total:'+str(lb.size()-1)

a=ac.Account()

f1=Frame(win)
Label(f1,text="Content :",font="Alial 16 bold").grid(row=0,column=0)
con=Entry(f1,bg="pink",font="Alial 16 bold").grid(row=0,column=1)
Label(f1,text="Price :",font="Alial 16 bold").grid(row=1,column=0)
pri=Entry(f1,bg="pink",font="Alial 16 bold").grid(row=1,column=1)
f1.pack()

f2=Frame(win)
b1=Button(f2,text="deposit",bg="light gray",command=deposit,font="Alial 16 bold").grid(row=0,column=0)
b2=Button(f2,text="withdraw",bg="light gray",command=withdraw,font="Alial 16 bold").grid(row=0,column=1)
f2.pack()
lbl=Label(win,text="total:0",font="Alial 10 bold").pack()

lb=Listbox(win,bg="white",width=10,font="helvelica 16 bold")
lb.insert(END,"Content    Price     Balance")
lb.pack(fill=BOTH)

win.mainloop()
