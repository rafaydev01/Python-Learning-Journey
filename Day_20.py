name = input("what is your name?")
age = input("what is your age?")



fahrenheit = float(input("enter temperature in fahrenheit:"))

celsius = (fahrenheit - 32) * 5/9

print("celsisus:", celsius)

# ==========================================
# Author: Abdul Rafay
# Topic: Python Lesson 1 - Variables & I/O
# Purpose: Greeting Program for GitHub
# ==========================================

# 1. Storing the name in a variable
developer_name = "Abdul Rafay"

# 2. Printing a dynamic welcome message
print("=========================================")
print(f" Hello World! Welcome to my GitHub.")
print(f" This repository belongs to: {developer_name}")
print("=========================================")

# 3. Interactive section for users visiting your GitHub
visitor_name = input("Please enter your name: ")
print(f"Nice to meet you, {visitor_name}! Thanks for checking out my code.")
