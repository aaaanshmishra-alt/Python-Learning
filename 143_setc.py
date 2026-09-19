# ============================================================
# PRACTICE PROBLEM 1 — SET COMPREHENSION
# ============================================================

# Problem:
# Given a list of numbers, create a SET containing the
# square of every number.
#
# Remember:
# A SET automatically removes duplicate values.
#
# Input:
# numbers = [1, 2, 2, 3, 4, 4, 5]
#
# Expected Output:
# {1, 4, 9, 16, 25}
#
# Hint:
# Use:
# {expression for item in collection}
#
# Write your solution below:
# ============================================================

numbers = [1, 2, 2, 3, 4, 4, 5]
result = {x * x for x in numbers}
print(result)