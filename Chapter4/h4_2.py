num=int(input("Enter a number : "))
rnum=0 #reversed number

while num>0:
    r=num%10
    rnum=(rnum*10)+r
    num//=10

print("Reverse of the number :",rnum)
