a=int(input("Enter the First Value : "))
b=int(input("Enter the Second Value : "))

if a>b:
    max=a
else:
    max=b

#Find least common multiple
while True:
    if max%a==0 and max%b==0:
        print("LCM of {} and {} = {}".format(a,b,max))
        break
    max+=1
