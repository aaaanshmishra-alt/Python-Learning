# Problem 5: Count Students With a Specific Mark
#
# Write a function:
# count_marks(students, target)
#
# - takes a dictionary containing student names and marks.
# - takes a target mark.
# - counts how many students received exactly that mark.
# - returns the count.
#
# Example:
# count_marks({
#     "Ansh": 85,
#     "Rahul": 90,
#     "Aman": 85,
#     "Riya": 70
# }, 85)
#
# should return 2
def count_marks(students, target):
    count = 0

    for marks in students.values():
        if marks == target:
            count = count + 1
    return count
print(count_marks({
    "Ansh": 85,
    "Rahul": 90,
    "Aman": 85,
    "Riya": 70
}, 85))