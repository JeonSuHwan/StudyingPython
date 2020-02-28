s1 = float(input("Enter the First side of a Triangle : "))
s2 = float(input("Enter the Second side of a Triangle : "))
s3 = float(input("Enter the Third side of a Triangle : "))

perimeter = s1+s2+s3
sp = perimeter/2 #semi perimeter
area=(sp*(sp-s1)*(sp-s2)*(sp-s3))**0.5

print("The Perimeter of Triangle =","%6.2f" %perimeter)
print("The Semi Perimeter of Triangle =","%6.2f" %sp)
print("The Area of a Triangle =","%6.2f" %area)
