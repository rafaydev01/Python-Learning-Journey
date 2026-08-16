# ==========================================
# 1. PYTHON LISTS (Mutable & Ordered)
# ==========================================

# Creating a list
fruits = ["apple", "banana", "cherry"]

# Accessing items (Zero-indexed)
first_fruit = fruits[0]  # "apple"
last_fruit = fruits[-1]  # "cherry"

# Modifying a list
fruits[1] = "blueberry"  # Changes "banana" to "blueberry"
fruits.append("orange")  # Adds to the end
fruits.insert(1, "mango")  # Inserts at index 1

# Removing items
fruits.remove("apple")  # Removes specific item
popped_item = fruits.pop()  # Removes and returns last item


# ==========================================
# 2. PYTHON TUPLES (Immutable & Ordered)
# ==========================================

# Creating a tuple
coordinates = (10.0, 20.0, 30.0)
single_item_tuple = ("solo",)  # Note the trailing comma

# Accessing items
latitude = coordinates[0]

# Tuples cannot be changed. The line below would cause a TypeError:
# coordinates[0] = 15.0 


# ==========================================
# 3. CONDITIONS (If, Elif, Else)
# ==========================================

# Checking conditions with list values
if "mango" in fruits:
    print("Mango is in the list!")
elif "blueberry" in fruits:
    print("Blueberry is available.")
else:
    print("Fruit not found.")

# Checking sizes and comparisons
list_length = len(fruits)
tuple_length = len(coordinates)

if list_length > tuple_length:
    print("The list has more items than the tuple.")
    
    # Nested condition
    if list_length == 3:
        print("The list has exactly 3 items.")
        
elif list_length < tuple_length:
    print("The tuple has more items.")
else:
    print("Both collections have the same size.")
