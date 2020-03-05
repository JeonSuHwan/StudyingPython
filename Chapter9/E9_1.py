#calculator

#addition
def add(a,b):
    return a+b
#subtraction
def sub(a,b):
    return a-b
#multiply
def mul(a,b):
    return a*b
#division
def div(a,b):
    return a/b

while True:
    choice=input("Enter choice(1.add/2.subtract/3.multiply/4.divide)/0.exit: ")

    if choice=='0':
        break
    
    if choice==1 or choice==2 or choice==3 or choice==4:
        n1=int(input("Enter first number: "))
        n2=int(input("Enter second number: "))

        if choice=='1':
            print("{} + {} = {}".format(n1,n2,add(n1,n2)))
        elif choice=='2':
            print("{} - {} = {}".format(n1,n2,sub(n1,n2)))
        elif choice=='3':
            print("{} * {} = {}".format(n1,n2,mul(n1,n2)))
        else:
            print("{} / {} = {}".format(n1,n2,div(n1,n2)))

    else:
        print("Wrong value, Try again!")
