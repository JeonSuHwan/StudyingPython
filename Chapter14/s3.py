#Program to deposit and withdrawal

#Display Locale format specifier
import locale

locale.setlocale(locale.LC_ALL,'')

class Operator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        if b==0:
            return 0
        else:
            return a/b

class Account(Operator):
    def __init__(self,bal=0):
        self.bal=bal
    def setBalance(self,bal):
        self.bal=bal
    def getBalance(self):
        return locale.format_string("%.f",self.bal,1)
    def numFormat(self,num):
        return locale.format_string("%.f",num,1)
    def deposit(self,dep):
        print("deposit",self.numFormat(dep))
        self.bal=super().add(self.bal,dep)
    def withdraw(self,wd):
        print("withdraw",self.numFormat(wd))
        self.bal=super().sub(self.bal,wd)

a=Account()
print("balance",a.getBalance())
a.deposit(30000)
print("balance",a.getBalance())
a.withdraw(20000)
print("balance",a.getBalance())
