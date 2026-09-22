# Problem Statement — Student Marks Analyzer

# Write a Python program to create a Student Marks Analyzer.

# The program should:
#
# 1. Take the name and marks of 5 students as input.
# 2. Store the student names and marks in a dictionary.
# 3. Display all students along with their marks.
# 4. Calculate and display the average marks of all students.
# 5. Find and display the student with the highest marks.
# 6. Find and display the student with the lowest marks.
# 7. Display all students who scored 75 or above.
# 8. Create a dictionary comprehension containing only students
#    who scored 75 or above.
# 9. Create a list comprehension containing all marks that are below 50.
# 10. Display the final results clearly.

# Restrictions:
#
# - Do not use max() or min().
# - Do not use external libraries.
# - Use loops and conditional statements to find the highest and lowest marks.
# - Use dictionary and list comprehensions where specifically requested.

# Topics:
# Dictionary, loops, conditions, input, list comprehension,
# dictionary comprehension, arithmetic, and output formatting.
students = {}

for i in range(5):
    name = input(f"Enter name of student {i + 1}: ")
    marks = float(input(f"Enter marks of {name}: "))
    students[name] = marks

print("\nStudent Marks:")
for name, marks in students.items():
    print(f"{name}: {marks}")

total = 0

for marks in students.values():
    total += marks

average = total / len(students)

highest_name = ""
highest_marks = -1

lowest_name = ""
lowest_marks = 101

for name, marks in students.items():
    if marks > highest_marks:
        highest_marks = marks
        highest_name = name

    if marks < lowest_marks:
        lowest_marks = marks
        lowest_name = name

above_75 = {name: marks for name, marks in students.items() if marks >= 75}

below_50 = [marks for marks in students.values() if marks < 50]

print(f"\nAverage Marks: {average:.2f}")
print(f"Highest: {highest_name} - {highest_marks}")
print(f"Lowest: {lowest_name} - {lowest_marks}")
print(f"Students scoring 75 or above: {above_75}")
print(f"Marks below 50: {below_50}")