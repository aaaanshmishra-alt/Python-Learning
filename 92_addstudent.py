# Problem 2: Add a Student
#
# Write a function:
# add_student(students, name, marks)
#
# - takes a dictionary of students and their marks.
# - takes a new student's name and marks.
# - adds the new student to the dictionary.
# - returns the updated dictionary.
#
# Example:
# add_student({"Ansh": 85, "Rahul": 90}, "Aman", 78)
# should return:
# {"Ansh": 85, "Rahul": 90, "Aman": 78}

def add_student(students, name, marks):
    students[name] = marks
    return students
print(add_student({"Ansh": 85, "Rahul": 90}, "Aman", 78))