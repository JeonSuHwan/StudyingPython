cost=int(input("Enter the actual cost: "))
amount=int(input("Enter the sales amount: "))

#compare cost and amount
if cost<amount:
    print("Total Profit =",float(amount-cost))
elif cost>amount:
    print("Total Loss Amount =",float(cost-amount))
else:
    print("No Profit No Loss!!!")
