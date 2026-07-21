# --- 1. Variables & Data Types ---
name = "Shradha"      # String (str)
age = 25              # Integer (int)
price = 99.99         # Float
is_following = True   # Boolean (bool)
a = None              # NoneType

print(type(name), type(age), type(price), type(is_following))

# --- 2. Taking Input & Type Conversion ---
# Inputs are always captured as a string by default
val1 = int(input("Enter first number: ")) 
val2 = int(input("Enter second number: "))
sum_res = val1 + val2
print("The sum is:", sum_res)

# --- Lecture 1 Practice Problems ---

# Problem 1: Write a program to input 2 numbers & print their sum.
num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))
print("Sum =", num1 + num2)

# Problem 2: Side of a square input & print its area.
side = float(input("Enter square side: "))
print("Area of square =", side * side)

# Problem 3: Input 2 floating-point numbers and print their average.
a = float(input("Enter first float: "))
b = float(input("Enter second float: "))
print("Average =", (a + b) / 2)

# Problem 4: Input 2 int numbers, a and b. Print True if a is greater than or equal to b.
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(a >= b)
