# 1. Output and Basic Printing
print("Hello World!")
print("Welcome to Python Lesson 1.")

# 2. Variables and Data Types
name = "Sharada"       # String
age = 22               # Integer
price = 99.99          # Float
is_learner = True      # Boolean
a = None               # None Type

# Printing variables and their types
print("Name:", name, "| Type:", type(name))
print("Age:", age, "| Type:", type(age))
print("Price:", price, "| Type:", type(price))

# 3. Basic Arithmetic Operations
sum_val = age + 5
print("Age after 5 years:", sum_val)

# 4. Taking User Input and Type Casting
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))  # Converting string input to integer

print("Hello " + user_name + ", you are " + str(user_age) + " years old.")
