# ============================================================
# PRACTICE PROBLEM 5 — IF-ELSE + TRANSFORMATION
# ============================================================

# Problem:
# Given a list of numbers, create a new list where:
#
# - If the number is EVEN → multiply it by 2
# - If the number is ODD  → multiply it by 3
#
# You must use LIST COMPREHENSION with IF-ELSE.
#
# Input:
# numbers = [1, 2, 3, 4, 5, 6]
#
# Expected Output:
# [3, 4, 9, 8, 15, 12]
#
# Hint:
# [value_if_true if condition else value_if_false
#  for item in collection]
#
# Write your solution below:
# ============================================================

numbers = [1, 2, 3, 4, 5, 6]
result = [x * 2 if x % 2 == 0 else x * 3 for x in numbers]
print(result)