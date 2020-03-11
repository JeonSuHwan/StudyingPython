import math as m

class Circle:
    def __init__(self,radius):
        self.radius=radius
    def cCircumf(self):
        return self.radius*2*m.pi
    def cArea(self):
        return (self.radius**2)*m.pi

rad=int(input("radius? : "))
c=Circle(rad)

print("radius :",c.radius)
print(c.cCircumf())
print(c.cArea())
