words=['seoul',"tokyo","moskoba","toronto","queensland","beijing","rome"]

sname=[i for i in words if len(i)>5] # satisfy name
slen=[len(i) for i in words if len(i)>5] #satisfy length

print("satisfy name    :",sname)
print("satisfy length    : ",slen)
