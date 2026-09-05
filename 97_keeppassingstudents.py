# Problem 7: Keep Passing Students
# Write a function:
# get_passed_students(students)
# - takes a dictionary containing student names and marks.
# - creates and returns a NEW dictionary.
# - keeps only students who scored 40 or more.
# - the original dictionary should not be changed.
#
# Example:
# get_passed_students({
#     "Ansh": 85,
#     "Rahul": 35,
#     "Aman": 60,
#     "Riya": 30
# })
#
# should return:
# {"Ansh": 85, "Aman": 60}
def get_passed_student(students):
    passed = {}

    for name, marks in students.items():
        if marks >= 40:
            passed[name] = marks
    return passed
print(get_passed_student({
    "Ansh": 85,
    "Rahul": 35,
    "Aman": 60,
    "Riya": 30
}))