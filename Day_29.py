# ==========================================
# PYTHON LESSON 1 & 2: LEARNING PROJECT
# Topic: Variables, Inputs, Conditions & Strings
# Target Output: Print the name 'Rafay'
# ==========================================

# --- LESSON 1: Variables and Data Types ---
# Storing different types of data in variables
course_name = "Python Programming"
lesson_one = "Variables and Inputs"
lesson_two = "Conditionals and String Formatting"
total_lessons = 2
is_easy = True

print("--- Welcome to Shadar Didi's Python Class ---")
print("Course: " + course_name)
print("Today we combine Lesson 1 (" + lesson_one + ") and Lesson 2 (" + lesson_two + ").")
print("")

# --- LESSON 2: User Input and Math Operations ---
# Taking a number input from the user to do a small calculation
print("[Activity 1: Math Magic]")
steps_learned_today = input("How many lines of code have you written today? ")
# Converting string input to integer
steps_count = int(steps_learned_today)
total_code_lines = steps_count + 15  # Adding bonus lines for practice

print("With bonus practice, your total lines will be: " + str(total_code_lines))
print("")

# --- LESSON 2: Conditional Statements (If-Else) ---
# Checking a condition based on the user's progress
print("[Activity 2: Progress Check]")
if total_code_lines > 20:
    status = "Excellent"
    print("Status: " + status + "! You are moving fast.")
else:
    status = "Good"
    print("Status: " + status + ". Keep practicing every day.")

print("")

# --- FINAL TASK: String Manipulation & Printing the Name ---
# Creating the final message using variables to print the target name
first_part = "This beautiful Python code was successfully generated for "
student_name = "Rafay"  # The requested name
celebration_emoji = "🎉"

# Combining everything into one long final message
final_report = first_part + student_name + " " + celebration_emoji

print("--- FINAL RESULT ---")
print(final_report)
print("Great job, " + student_name + "! Lesson 1 and 2 are complete.")
