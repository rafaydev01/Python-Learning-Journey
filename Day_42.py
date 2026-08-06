marks = int(input("enter marks :"))

if(marks >= 90):
    grade = "A"
elif(marks >= 80):
    grade = "B"
elif(marks >= 70):
    grade = "C"
else:
    grade = "D"

print("Grade:",grade)                


num = int(input("enter number :"))

if(num % 2 == 0):
    print("EVEN")
else:
    print("ODD") 


a = int(input("enter first number"))
b = int(input("enter second number"))
c = int(input("enter third number"))


if(a >= b and a >= b):
    print("number a is the largest",a)
elif(b >= c):
    print("number second is the largest",b)
else:
    print("number third is the largest")        
    