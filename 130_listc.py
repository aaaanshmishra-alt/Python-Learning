# ============================================================
# PRACTICE PROBLEM 3 — FILTER + TRANSFORM
# ============================================================

# Problem:
# Given a list of numbers, create a new list containing
# the SQUARE of ONLY the EVEN numbers.
#
# You must use LIST COMPREHENSION.
#
# Input:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
#
# Expected Output:
# [4, 16, 36, 64]
#
# Hint:
# 1. First filter the even numbers.
# 2. Then square those numbers.
#
# Use the structure:
# [expression for item in collection if condition]
#
# Write your solution below:
# ============================================================
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = [x * x for x in numbers if x % 2 == 0]
print(result)