#Read two integers
a=int(input("Please enter a number : "))
b=int(input("Please enter a number : "))

#Find factors
aset={i for i in range(1,a+1) if a%i==0}
bset={i for i in range(1,b+1) if b%i==0}

#print sets
print(aset)
print(bset)

#print common factor
print("Common factor :",aset&bset)

