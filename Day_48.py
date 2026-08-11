# 1. Define a list of numbers
numbers = [12, 5, 8, 23, 19, 42, 3, 10]

# Create empty lists to sort the numbers based on conditions
even_numbers = []
odd_numbers = []

print(f"Original list: {numbers}")
print("-" * 30)

# 2. Loop through the list and use conditional statements
for num in numbers:
    # Condition 1: Check if the number is even
    if num % 2 == 0:
        even_numbers.append(num)
        print(f"{num} is Even.")
        
    # Condition 2: Check if the number is odd
    else:
        odd_numbers.append(num)
        print(f"{num} is Odd.")

print("-" * 30)
print(f"List of Even Numbers: {even_numbers}")
print(f"List of Odd Numbers: {odd_numbers}")


# 3. Checking for specific conditions inside a list using the 'in' keyword
search_fruit = "mango"
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

if search_fruit in fruits:
    print(f"\nSuccess: Yes, '{search_fruit}' is in the fruits list!")
else:
    print(f"\nError: '{search_fruit}' was not found.")


# 4. Advanced: List Comprehension with conditions (Short and efficient)
# This creates a new list with only numbers greater than 10
large_numbers = [x for x in numbers if x > 10]
print(f"Numbers greater than 10: {large_numbers}")
