# ============================================================
# PHASE 4 — LAMBDA FUNCTIONS
# QUESTION 6: FILTER ELIGIBLE STUDENTS
# ============================================================
#
# PROBLEM STATEMENT:
#
# You are given a list of students' marks:
#
# marks = [35, 78, 42, 90, 28, 65, 50]
#
# REQUIREMENTS:
#
# 1. Create a lambda function named check_pass.
#
# 2. It must accept one argument, mark.
#
# 3. Return True if the mark is greater than or equal to 40.
#    Otherwise, return False.
#
# 4. Call check_pass() with 35, 78, and 40.
#
# 5. Print the result of each call.
#
# EXPECTED OUTPUT:
#
# False
# True
# True
#
# RULES:
#
# - Use lambda, not def.
# - Use the comparison operator >=.
# - Do not hardcode the answers.
#
# ============================================================
# WRITE YOUR CODE BELOW
# ============================================================

marks = [35, 78, 42, 90, 28, 65, 50]
check_pass = lambda mark : mark >= 40

print(check_pass(35))

print(check_pass(78))

print(check_pass(40))