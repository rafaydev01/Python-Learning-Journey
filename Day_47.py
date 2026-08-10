

# 1. CREATING A LIST
# Lists are defined using square brackets [] with items separated by commas
fruits = ["apple", "banana", "cherry", "date"]
mixed_list = [42, "hello", True, 3.14]  # Lists can hold different data types
empty_list = []

print("Original fruits list:", fruits)


# 2. ACCESSING ITEMS
# Python uses zero-based indexing (the first item is at index 0)
print("First fruit:", fruits[0])   # Output: apple
print("Third fruit:", fruits[2])   # Output: cherry

# Negative indexing counts from the end (-1 is the last item)
print("Last fruit:", fruits[-1])   # Output: date

# Slicing extracts a range of items (start index is inclusive, end is exclusive)
print("First three fruits:", fruits[0:3]) # Output: ['apple', 'banana', 'cherry']


# 3. MODIFYING ITEMS
# Change an item by referencing its index
fruits[1] = "blueberry"
print("After modification:", fruits)


# 4. ADDING ITEMS
# Add an item to the end of the list
fruits.append("elderberry")

# Insert an item at a specific index
fruits.insert(1, "banana") 

# Add elements from another list
fruits.extend(["fig", "grape"])
print("After adding items:", fruits)


# 5. REMOVING ITEMS
# Remove a specific item by its value
fruits.remove("cherry")

# Remove an item at a specific index (or the last item if left blank)
popped_fruit = fruits.pop(3) 

# Delete an item using the 'del' keyword
del fruits[0] 

print(f"After removals (popped '{popped_fruit}'):", fruits)


# 6. USEFUL LIST FUNCTIONS
print("Number of items in list:", len(fruits)) # Get list length
fruits.sort() # Sort the list alphabetically/numerically
print("Sorted list:", fruits)


# 7. LOOPING THROUGH A LIST
print("\nLooping through the fruits:")
for fruit in fruits:
    print(f"- I love eating {fruit}")