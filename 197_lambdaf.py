# ============================================================
# PHASE 4 — LAMBDA FUNCTIONS
# QUESTION 5: SORT STUDENTS BY MARKS
# ============================================================
#
# PROBLEM STATEMENT:
#
# You are given a list of dictionaries representing students.
#
# students = [
#     {"name": "Ansh", "marks": 85},
#     {"name": "Rahul", "marks": 72},
#     {"name": "Priya", "marks": 93},
#     {"name": "Aman", "marks": 68}
# ]
#
# REQUIREMENTS:
#
# 1. Use sorted() to sort the students by their marks.
#
# 2. Sort them from highest marks to lowest marks.
#
# 3. Use a lambda function with the key parameter.
#
# 4. Store the sorted list in a variable named result.
#
# 5. Print result.
#
# HINTS:
#
# - student["marks"] accesses the marks of one student.
# - sorted() supports reverse=True for descending order.
#
# EXPECTED ORDER:
#
# Priya: 93
# Ansh: 85
# Rahul: 72
# Aman: 68
#
# RULES:
#
# - Use lambda, not def.
# - Do not manually rearrange the dictionaries.
# - Do not hardcode the sorted result.
#
# ============================================================
# WRITE YOUR CODE BELOW
# ============================================================
students = [
   {"name": "Ansh", "marks": 85},
    {"name": "Rahul", "marks": 72},
   {"name": "Priya", "marks": 93},
   {"name": "Aman", "marks": 68}
]
result = sorted(students,key = lambda students : students["marks"], reverse = True)
print(result)