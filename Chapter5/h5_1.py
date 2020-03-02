slist=[] #list

while True:
    want=input("Please enter what you want : ")

    if want=="quit":
        break
    
    slist.append(want) #append and sort
    slist.sort()
    for i,value in enumerate(slist): #Print the list
        print(i+1,value)

