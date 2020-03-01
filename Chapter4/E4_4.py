low=int(input("Enter the lower limit for the range : "))
up=int(input("Enter the upper limit for the range : "))

#if the number is odd, print it.
for i in range(low,up+1):
    if i%2==1:
        print(i)
