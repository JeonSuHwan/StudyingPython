test=[57,99,78,85,60]

print("Output>")
for i,value in enumerate(test):
    if value>=70:
        print("No.{} your score is {}, pass!".format(i+1,value))
    else:
        print("No.{} your score is {}, fail!".format(i+1,value))
