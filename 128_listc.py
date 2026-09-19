# ============================================================
# PRACTICE PROBLEM 1 — LIST COMPREHENSION
# ============================================================

# Problem:
# Given a list of numbers, create a new list containing
# the square of every number using LIST COMPREHENSION.
#
# You must NOT use a normal for loop.
#
# Input:
# numbers = [2, 4, 6, 8, 10]
#
# Expected Output:
# [4, 16, 36, 64, 100]
#
# Hint:
# Use the basic list comprehension structure:
#
# [expression for item in collection]
#
# Write your solution below:
# ============================================================

numbers = [2, 4, 6, 8, 10]
result = [x * x for x in numbers]
print(result)