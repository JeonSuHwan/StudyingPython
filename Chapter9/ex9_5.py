n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))

def qR(a,b):
    return a//b,a%b

quo,rem=qR(n1,n2)
print("quotient: {}, remainder: {}".format(quo,rem))
