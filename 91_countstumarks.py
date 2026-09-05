# Problem 1: Find a Student's Marks
#
# Write a function:
# get_marks(student, name)
#
# - takes a dictionary containing student names and their marks.
# - takes a student's name as a parameter.
# - returns that student's marks.
#
# Example:
# get_marks({"Ansh": 85, "Rahul": 90, "Aman": 78}, "Rahul")
# should return 90

def get_marks(student, name):
    return student[name]
print(get_marks({"Ansh": 85, "Rahul": 90, "Aman": 78}, "Rahul"))
    