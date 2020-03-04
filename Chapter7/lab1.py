print("Let's make a dinner time!!!")
print("You must input 5 times!!!")

dlist=[]

for i in range(5):
    ingre=input("Please enter a dinner ingredient : ") #Read the dinner ingridients
    dlist.append(ingre)
    dlist.sort() #Sort the list

for i in dlist:
    print(dlist.index(i)+1,i)
