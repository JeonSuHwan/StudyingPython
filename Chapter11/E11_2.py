class Car:
    def __init__(self,name,speed):
        self.name=name
        self.speed=speed
    def getName(self):
        return self.name
    def getSpeed(self):
        return self.speed

car1=Car("Audi",10)
car2=Car("BMW",30)

print("{}'s speed is {}".format(car1.getName(),car1.getSpeed()))
print("{}'s speed is {}".format(car2.getName(),car2.getSpeed()))

#Change the speed of cars
car1.speed=20
car2.speed=40

print()
print("{}'s speed is {}".format(car1.getName(),car1.getSpeed()))
print("{}'s speed is {}".format(car2.getName(),car2.getSpeed()))

del car1.speed
def car1
