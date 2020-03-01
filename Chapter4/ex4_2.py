total=0
number=int(input("Enter any integer below 10: "))

while number<=10:
    total+=number
    number+=1
    print("Total =",total)
else:
    print("Your value is greater than 10.")
