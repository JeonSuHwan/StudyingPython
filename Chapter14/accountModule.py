#Program to desposit and withdraw

import locale
locale.setlocale(locale.LC_ALL,'')

class Operator:
    def add(self,a,b): #addition
        return a+b
    def sub(self,a,b): #subtraction
        return a-b
    def mul(self,a,b): #multiplication
        return a*b
    def div(self,a,b): #division
        if b==0:
            return 0
        else:
            return a/b

class Account(Operator):
    #Set the initial balance
    def __init__(self,bal=0):
        self.bal=bal
    #Set the balance
    def setBalance(self,bal):
        self.bal=bal
    #Get the current balance
    def getBalance(self,bal):
        return locale.format_string("%.f",self.bal,1)
    #Number format
    def numFormat(self,num):
        return locale.format_string("%.f",num,1)
    #add the deposit to balance
    def deposit(self,dep):
        self.bal=super().add(self.bal,dep)
        print("deposit",self.numFormat(dep))
    #subtract the withdraw to balance
    def withdraw(self,wd):
        self.bal=super().sub(self.bal,wd)
        print("withdraw",self.numFormat(wd))
