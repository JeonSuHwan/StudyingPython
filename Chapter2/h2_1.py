radius = int(input("Please Enter the Radius of a Cylinder : "))
height = int(input("Please Enter the Height of a Cylinder : "))
Pi=3.14
volume=Pi*(radius**2)*height
surface=2*Pi*(radius**2)+2*Pi*radius*height

print("The Surface Area of a Cylinder = {}".format(surface))
print("The Volume of a Cylinder = {}".format(volume))
