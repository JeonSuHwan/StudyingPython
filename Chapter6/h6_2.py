a={i for i in range(1,101) if i%3==0}
b={i for i in range(1,101) if i%5==0}

print(a)
print(b)
c=a&b
print(c)
print(sorted(c))
