# ============================================================
# FINAL PRACTICE: STUDENT GRADE REPORT USING **KWARGS
# ============================================================
#
# Create a function named grade_report() that accepts any
# number of keyword arguments using **kwargs.
#
# Each keyword argument represents a student's name and marks.
#
# REQUIREMENTS:
# 1. Accept any number of keyword arguments.
# 2. For every student, check their marks.
# 3. If marks are 90 or above, print "Excellent".
# 4. If marks are 60 or above but below 90, print "Good".
# 5. If marks are 40 or above but below 60, print "Pass".
# 6. If marks are below 40, print "Fail".
# 7. Return the total number of students who passed.
#    Students with marks of 40 or above are considered passed.
#
# EXAMPLE:
# Input:
# grade_report(Ansh=95, Rahul=32, Priya=75, Aman=45, Neha=60)
#
# Expected output:
# Ansh : Excellent
# Rahul : Fail
# Priya : Good
# Aman : Pass
# Neha : Good
#
# Total students passed: 4
#
# HINTS:
# 1. Use **kwargs in the function definition.
# 2. Use kwargs.items() to access student names and marks.
# 3. Use if, elif and else to classify the marks.
# 4. Maintain a counter for students who passed.
# 5. Return the final count.
#
# Do not hardcode the student names or marks inside the function.
#
# ============================================================
def grade_report(**kwargs):
    count = 0
    for name , values in kwargs.items():
        if values >= 90 :
            print(name, ":", "Excellent")
        elif values >= 60:
            print(name, ":","Good")
        elif values >= 40 :
            print(name, ":", "Pass")
        else:
            print(name,":", "Fail")
        if values >= 40:
            count = count + 1
    return count
new = grade_report(Ansh=95, Rahul=32, Priya=75, Aman=45, Neha=60)
print("Number of students passed: ", new)
