score=[73,95,80,57,99]

#compute the sum of scores
def func_sum(s):
    sum=0
    for i in s:
        sum+=i
    return sum

total=func_sum(score)
print("Total score :",total)
print("Average score :",total/len(score))
    
