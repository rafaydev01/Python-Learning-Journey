# GitHub Profile: Abdul Rafay
# Topic: Variables, Conditions, Lists, and Tuples

# 1. Variables and Tuples (Immutable data)
user_name = "Abdul Rafay"
account_info = ("abdulrafay_git", "Joined 2026")  # Updated join date to 2026

# 2. Lists (Mutable data)
programming_languages = ["Python", "JavaScript", "C++", "HTML/CSS"]

# 3. Conditional Logic
print(f"Developer Name: {user_name}")
print(f"GitHub Handle: {account_info[0]}")
print(f"Account Status: {account_info[1]}")

# Check languages and display status
if not programming_languages:
    print(f"{user_name} has not added any languages yet.")
elif "Python" in programming_languages and "2026" in account_info[1]:
    print(f"{user_name} is a New Python Developer who joined in 2026.")
    print("Current Tech Stack:")
    for lang in programming_languages:
        print(f" - {lang}")
else:
    print(f"{user_name} is exploring different technologies.")
