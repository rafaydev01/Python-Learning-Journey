# ==============================================================================
# STUDENT PERFORMANCE TRACKER & DATA PROCESSING SYSTEM
# Demonstrates advanced manipulation of lists, conditions, and tuples in Python
# ==============================================================================

# Input Data: A list of tuples containing student information
# Format: (Student_ID, Name, Major, [List of Exam Scores], Attendance_Rate)
raw_student_data = [
    (101, "Alice Smith", "Computer Science", [88, 92, 79, 95], 0.94),
    (102, "Bob Jones", "Mathematics", [55, 60, 48, 62], 0.88),
    (103, "Charlie Brown", "Computer Science", [92, 96, 94, 99], 0.98),
    (104, "David Miller", "Physics", [72, 68, 74, 70], 0.75),
    (105, "Eva Green", "Mathematics", [85, 81, 89, 78], 0.91),
    (106, "Frank Wright", "Computer Science", [45, 50, 52, 40], 0.62),
    (107, "Grace Lee", "Physics", [90, 93, 88, 91], 0.96),
]


def calculate_grade(average_score, attendance):
    """Determines final grade letter based on score and attendance conditions."""
    if attendance < 0.75:
        return "Fail (Low Attendance)"
    elif average_score >= 90:
        return "A"
    elif average_score >= 80:
        return "B"
    elif average_score >= 70:
        return "C"
    elif average_score >= 50:
        return "Pass"
    else:
        return "Fail"


# 1. PROCESS AND TRANSFORM DATA
# We use a list comprehension to parse the raw data.
# Condition inside: It processes the metrics dynamically.
# Output: A new list of tuples with computed data.
processed_students = []
for student in raw_student_data:
    student_id, name, major, scores, attendance = student

    # Calculate average score using standard list functions
    avg_score = sum(scores) / len(scores)

    # Apply conditional logic function
    final_status = calculate_grade(avg_score, attendance)

    # Append a new structured tuple to our list
    processed_students.append((student_id, name, major, avg_score, final_status))


# 2. FILTER DATA USING LIST COMPREHENSIONS (CONDITIONS)
# Filter 1: Honor Roll Students (Major is Computer Science AND Grade is 'A')
honor_roll_cs = [
    (name, major, avg)
    for s_id, name, major, avg, grade in processed_students
    if major == "Computer Science" and grade == "A"
]

# Filter 2: Students who are at risk of failing (Status contains 'Fail')
at_risk_students = [
    (name, major, grade)
    for _, name, major, _, grade in processed_students
    if "Fail" in grade
]


# 3. GENERATE STATISTICS BY GROUPING
# Separate math scores based on a conditional filter
math_scores = [
    avg
    for _, _, major, avg, _ in processed_students
    if major == "Mathematics"
]
avg_math_score = sum(math_scores) / len(math_scores) if math_scores else 0


# ==============================================================================
# DISPLAY RESULTS
# ==============================================================================
print("=" * 65)
print(f"{'ID':<6}{'NAME':<16}{'MAJOR':<18}{'AVG SCORE':<12}{'STATUS'}")
print("=" * 65)

for s_id, name, major, avg, grade in processed_students:
    print(f"{s_id:<6}{name:<16}{major:<18}{avg:<12.1f}{grade}")

print("=" * 65)
print(f"CS Honor Roll (Tuples): {honor_roll_cs}")
print(f"At Risk Students (Tuples): {at_risk_students}")
print(f"Average Mathematics Score: {avg_math_score:.1f}")
print("=" * 65)
