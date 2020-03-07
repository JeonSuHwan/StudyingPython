import time
from matching import *

list1=dataInput()
list2=dataInput()

print("shake for 3 seconds...")
time.sleep(3)
shake(list1)
shake(list2)

print()
print("congratulations~~~")
print()

#print result
for i in range(3):
    print(list1[i],"<---------->",list2[i])
