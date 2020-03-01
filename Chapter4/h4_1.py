num=int(input("Enter number : "))

count=0 #number of digits

while num>0:
    count+=1
    num//=10
print("The number of digits in the number is :",count)
