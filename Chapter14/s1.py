#Calculation program

class Operator:
    def __init__(self):
        self.a=1
        self.b=1
    def add(self,a,b): #addition
        self.a=a
        self.b=b
        return a+b
    def sub(self,a,b): #subtraction
        self.a=a
        self.b=b
        if a>=b:
            return self.a-self.b
        else:
            return self.b-self.a
    def mul(self,a,b): #multiplication
        self.a=a
        self.b=b
        return self.a*self.b
    def div(self,a,b): #division
        self.a=a
        self.b=b
        if b==0:
            return 0
        else:
            return self.a/self.b

op=Operator()
print("add :",op.add(20,10))
print("sub :",op.sub(20,10))
print("mul :",op.mul(20,10))
print("div :",op.div(20,10))


