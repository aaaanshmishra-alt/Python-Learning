# ============================================================
# PHASE 4 — LAMBDA FUNCTIONS
# QUESTION 8: STUDENT GRADING SYSTEM
# ============================================================
#
# PROBLEM STATEMENT:
#
# Create a lambda function named get_grade.
#
# REQUIREMENTS:
#
# 1. Accept one argument: marks.
#
# 2. Return grades according to these conditions:
#
#    Marks >= 90       -> "A"
#    Marks >= 75       -> "B"
#    Marks >= 60       -> "C"
#    Marks >= 40       -> "D"
#    Marks < 40        -> "Fail"
#
# 3. Test your lambda with:
#
#    get_grade(95)
#    get_grade(82)
#    get_grade(65)
#    get_grade(45)
#    get_grade(30)
#
# EXPECTED OUTPUT:
#
# A
# B
# C
# D
# Fail
#
# RULES:
#
# - Use lambda, not def.
# - Use conditional expressions.
# - Do not use normal if-elif-else statements.
#
# ============================================================
# WRITE YOUR CODE BELOW
# ============================================================
get_grade = lambda marks: "A" if marks >= 90 else "B" if marks >= 75 else "C" if marks >= 60 else "D" if marks >= 40 else "Fail"

print(get_grade(95))
print(get_grade(82))
print(get_grade(65))
print(get_grade(45))
print(get_grade(30))