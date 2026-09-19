# ============================================================
# PRACTICE PROBLEM 4 — IF-ELSE LIST COMPREHENSION
# ============================================================

# Problem:
# Given a list of numbers, create a new list where:
#
# - If the number is EVEN → put "Even"
# - If the number is ODD  → put "Odd"
#
# You must use LIST COMPREHENSION with IF-ELSE.
#
# Input:
# numbers = [10, 7, 4, 9, 2, 15]
#
# Expected Output:
# ["Even", "Odd", "Even", "Odd", "Even", "Odd"]
#
# Hint:
# [value_if_true if condition else value_if_false
#  for item in collection]
#
# Write your solution below:
# ============================================================
numbers = [10, 7, 4, 9, 2, 15]
result = ["Even" if x % 2 == 0 else "odd" for x in numbers]
print(result)