# Problem 3: Tuple Unpacking
#
# Write a function:
# get_student_info(student)
#
# - takes a tuple containing a student's name, age, and branch.
# - uses tuple unpacking to separate the three values.
# - returns the student's name and branch.
#
# Example:
# get_student_info(("Ansh", 20, "CSE"))
# should return:
# ("Ansh", "CSE")

def get_student_info(student):
    name, age, branch = student
    return name, branch
print(get_student_info(("Ansh", 20, "CSE")))
     