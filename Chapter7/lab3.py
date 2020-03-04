voted={"John":"True","Alice":"False","Rosa":"True"}

print(voted)
while True:
    name=input("Enter your name : ")
    if name=="":
        break

    if name in voted:
        if voted[name]=='True':
            print(name,"already voted!")
        elif voted[name]=='False':
            print(name,", please vote!")
            voted[name]="True"
    else:
        print(name,"has no voting rights.")
print()
print(voted)
