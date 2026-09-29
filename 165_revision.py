# ============================================================
# PROBLEM: Student Marks Analyzer
# ============================================================
#
# Write a Python program that:
#
# 1. Takes the number of subjects from the user.
#
# 2. Takes the marks of each subject and stores them in a list.
#
# 3. Create a function calculate_average(marks) that:
#       - Calculates and returns the average marks.
#
# 4. Create a function find_grade(average) that returns:
#       - "A" if average >= 90
#       - "B" if average >= 75
#       - "C" if average >= 60
#       - "D" if average >= 40
#       - "F" if average < 40
#
# 5. Find and display:
#       - Total marks
#       - Average marks
#       - Highest marks
#       - Lowest marks
#       - Grade
#
# 6. Also count how many subjects the student passed.
#    A subject is considered passed if marks >= 40.
#
# Example Input:
# Enter number of subjects: 5
# Enter marks: 85
# Enter marks: 72
# Enter marks: 91
# Enter marks: 68
# Enter marks: 79
#
# Example Output:
# Total Marks: 395
# Average Marks: 79.0
# Highest Marks: 91
# Lowest Marks: 68
# Passed Subjects: 5
# Grade: B
#
# NOTE:
# Use functions wherever mentioned above.
# Do not use any external libraries.
# ============================================================


# Write your code below

def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average

def find_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"

n = int(input("Enter number of subjects: "))

marks = []

for i in range(n):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

total = sum(marks)
average = calculate_average(marks)
highest = max(marks)
lowest = min(marks)

passed = 0

for mark in marks:
    if mark >= 40:
        passed += 1

grade = find_grade(average)

print("\n===== STUDENT RESULT =====")
print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Passed Subjects:", passed)
print("Grade:", grade)