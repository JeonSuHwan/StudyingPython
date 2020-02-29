#input grades
s1=int(input("Enter the score of subject 1: "))
s2=int(input("Enter the score of subject 2: "))
s3=int(input("Enter the score of subject 3: "))
s4=int(input("Enter the score of subject 4: "))
s5=int(input("Enter the score of subject 5: "))

#Calculate average
avg=(s1+s2+s3+s4+s5)/5

print("Average =",avg)
if avg>=90:
    print("Grade: A")
elif 80<=avg<90:
    print("Grade: B")
elif 70<=avg<80:
    print("Grade: C")
elif 60<=avg<70:
    print("Grade: D")
else:
    print("Grade: F")
