# Problem Statement — Student Grade Calculator
#
# Write a Python program to create a Student Grade Calculator.
#
# The program should:
#
# 1. Take the names of 5 students as input.
#
# 2. For each student, take marks in 3 subjects.
#
# 3. Store the data in a nested dictionary in the following format:
#
#    {
#        "Ansh": {
#            "Python": 85,
#            "Maths": 78,
#            "Physics": 90
#        }
#    }
#
# 4. Create a function that calculates the total marks
#    of a student.
#
# 5. Create a function that calculates the average marks
#    of a student.
#
# 6. Assign grades according to the average:
#
#    90 or above  -> A
#    75 to 89     -> B
#    60 to 74     -> C
#    50 to 59     -> D
#    Below 50     -> F
#
# 7. Display each student's:
#    - Name
#    - Total marks
#    - Average marks
#    - Grade
#
# 8. Find the student with the highest average.
#
# 9. Create a dictionary comprehension containing only
#    students who received grade A or B.
#
# 10. Create a list comprehension containing the names
#     of students who failed in at least one subject.
#
# Restrictions:
#
# - Use functions for total and average calculations.
# - Do not use max() or min() to find the highest student.
# - Use loops and conditional statements.
# - Use dictionary comprehension and list comprehension
#   where requested.
#
# Topics:
# Input, dictionaries, nested dictionaries, lists,
# functions, loops, conditions, dictionary comprehension,
# list comprehension, arithmetic and output formatting.

students = {}

for i in range(5):
    name = input(f"Enter student {i + 1} name: ")

    python = float(input("Enter Python marks: "))
    maths = float(input("Enter Maths marks: "))
    physics = float(input("Enter Physics marks: "))

    students[name] = {
        "Python": python,
        "Maths": maths,
        "Physics": physics
    }


def calculate_total(marks):
    return sum(marks.values())


def calculate_average(marks):
    return calculate_total(marks) / len(marks)


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


print("\nStudent Results")

highest_name = ""
highest_average = -1

for name, marks in students.items():
    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = calculate_grade(average)

    print(f"\nName: {name}")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")

    if average > highest_average:
        highest_average = average
        highest_name = name


grade_ab = {
    name: calculate_grade(calculate_average(marks))
    for name, marks in students.items()
    if calculate_grade(calculate_average(marks)) in ["A", "B"]
}


failed_students = [
    name
    for name, marks in students.items()
    if any(score < 50 for score in marks.values())
]


print(f"\nHighest Average: {highest_name} - {highest_average:.2f}")
print(f"Students with Grade A or B: {grade_ab}")
print(f"Students who failed in at least one subject: {failed_students}")