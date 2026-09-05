# Problem 3: Count Passed Students
#
# Write a function:
# count_passed(students)
#
# - takes a dictionary containing student names and marks.
# - counts how many students scored 40 or more.
# - returns the count.
#
# Example:
# count_passed({"Ansh": 85, "Rahul": 35, "Aman": 60, "Riya": 30})
# should return 2
#
# Because:
# Ansh → 85 → Passed
# Rahul → 35 → Failed
# Aman → 60 → Passed
# Riya → 30 → Failed
def count_passed(students):
    count = 0
    for marks in students.values():
        if marks >= 40:
            count = count + 1
    return count
print(count_passed({
    "Ansh": 85,
    "Rahul": 35,
    "Aman": 60,
    "Riya": 30
}))