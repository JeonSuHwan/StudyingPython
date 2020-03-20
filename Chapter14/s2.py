#Program to deposit and withdrawal
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
    def __init__(self,bal):
        self.bal=bal
    def setBalance(self,bal):
        self.bal=bal
    def getBalance(self):
        return self.bal
    def deposit(self,dep):
        print("deposit",dep)
        self.bal=super().add(self.bal,dep)
    def withdraw(self,wd):
        print("withdraw",wd)
        self.bal=super().sub(self.bal,wd)

a=Account(0)
print("balance",a.getBalance())
a.deposit(30000)
print("balance",a.getBalance())
a.withdraw(20000)
print("balance",a.getBalance())
