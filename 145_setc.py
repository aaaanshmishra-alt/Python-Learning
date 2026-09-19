# ============================================================
# PRACTICE PROBLEM 3 — SET COMPREHENSION
# ============================================================

# Problem:
# Given a list of numbers, create a SET containing the
# SQUARE of only the ODD numbers.
#
# Input:
# numbers = [1, 2, 3, 4, 5, 6, 7]
#
# Expected Output:
# {1, 9, 25, 49}
#
# Hint:
# 1. Filter the odd numbers.
# 2. Square those numbers.
#
# Use:
# {expression for item in collection if condition}
#
# Write your solution below:
# ============================================================

numbers = [1, 2, 3, 4, 5, 6, 7]
result = {x * x for x in numbers if x % 2 != 0}
print(result)