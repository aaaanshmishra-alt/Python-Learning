# Problem 6: Find Student With Highest Marks
#
# Write a function:
# top_student(students)
#
# - takes a dictionary containing student names and marks.
# - finds the student who has the highest marks.
# - returns the student's name.
#
# Example:
# top_student({
#     "Ansh": 85,
#     "Rahul": 90,
#     "Aman": 78,
#     "Riya": 95
# })
#
# should return "Riya"
def top_student(students):
    highest = list(students.values())[0]
    top_student = list(students.keys())[0]

    for name , marks in students.items():
        if marks > highest:
            highest = marks
            top_student = name
    return top_student
print(top_student({"Ansh": 85, "Rahul": 90, "Aman": 78, "Riya": 95}))
