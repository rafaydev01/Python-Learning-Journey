#day_2

print("My name is Abdul Rafay.", "My age is 16.")
#Variables
name = "Abdul Rafay"#string
age = 16 #int
price = 20.4 #float
age2 = age
age3 = age2
print("my name is :", name)
print(age3)
print("price is :", price)
#type
print(type(age))
print(type(name))
print(type(price))
#quotes
name1 = 'Abdul Rafay'
name2 = "abdul rafay"
name3 = '''Abdul Rafay'''

print(name1)
print(name2)
print(name3)
#boolean
age = 23
old = False
a = None

print(type(old))
print(type(a))

a = 6
b = 4
diff = a - b
print(diff)
#arithmetic operator
a = 9
b = 4
sum = a + b
diff = a - b

print(sum)
print(diff)
print(a / b)
print(a * b)
print( a % b)
print(a ** b)
#relational operator

a = 8
b = 4
print( a == b)
print(a != b)
print(a >= b)
print(a > b)
print(a <= b)
print(a < b)

#Assignment operator
# *= , += , -= ,%= , **=
num = 10
num = num + 10
print("num :", num)

num = 10
num -= 5
print("num:", num)

num = 5
num *= 5
print("num:", num)
#logical operator

a = 50
b = 30
print(not False)
print(not a > b)
#And operater

val1 = True
val2 = True
print("and operator", val1 and val2)

#OR operator
val1 = True
val2 = False
print("OR operator", val1 or val2)

a = 60
b = 30

print("or operator", (a == b) or (a > b))

#Type conversion
#we can not substrat string value from float
a = int("2")
b = 8.33
print(a + b)

#change float into str
a = 88.0
a = str(a)

print(type(a))
#
a = 3.9998
a = str(a)
print(type(a))
#Input from user 
name =input("your name is :")
age = input("your age is :")
marks = input("your marks is :")
print("wellcome", name)
print("your age is :", age)
print("your marks is :",marks)
