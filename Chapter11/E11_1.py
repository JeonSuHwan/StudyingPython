class Animal:
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound

dog=Animal("Dog","bow-wow!!")
cat=Animal("Cat","meow~~")

print(dog.name,"sounds",dog.sound)
print(cat.name,"sounds",cat.sound)
