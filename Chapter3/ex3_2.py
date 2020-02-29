radius = int(input("Enter radius : "))
if radius>=0:
    print("Area = {}".format(3.14*radius**2))
    print("Circumference = {}".format(2*3.14*radius))
else:
    print("Please enter a positive number.")
