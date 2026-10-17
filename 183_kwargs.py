# ============================================================
# PROBLEM: FILTER STUDENT MARKS USING **KWARGS
# ============================================================
#
# Create a function named filter_passed() that accepts any
# number of keyword arguments using **kwargs.
#
# Each keyword argument represents a student's name and marks.
#
# REQUIREMENTS:
# 1. Accept any number of keyword arguments.
# 2. Each value represents a student's marks out of 100.
# 3. A student passes if their marks are 40 or above.
# 4. Print the names and marks of students who passed.
# 5. Return the number of students who passed.
#
# EXAMPLE:
# Input:
# filter_passed(Ansh=85, Rahul=32, Priya=67, Aman=39, Neha=40)
#
# Expected output:
# Ansh : 85
# Priya : 67
# Neha : 40
#
# Number of students passed: 3
#
# HINTS:
# 1. Use **kwargs to collect student names and marks.
# 2. Iterate through kwargs.items() to access names and marks.
# 3. Use an if condition to check whether marks are >= 40.
# 4. Print each student who passed.
# 5. Maintain a counter for the number of students who passed.
# 6. Return the final count.
#
# Do not hardcode the students or their marks inside
# the function.
#
# ============================================================

def filter_passed(**kwargs):
    count = 0

    for name ,values in kwargs.items():
        if values >= 40:
            count = count + 1
            print(name, ":", values)
    return count
new = filter_passed(Ansh=85, Rahul=32, Priya=67, Aman=39, Neha=40)
print(filter_passed(Ansh=85, Rahul=32, Priya=67, Aman=39, Neha=40))
print("Number of students passed : ",new)