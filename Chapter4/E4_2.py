num=int(input("Enter a number : "))
factorial=1

for i in range(7,0,-1):
    factorial*=i
print("The factorial of {} is {}".format(num,factorial))
