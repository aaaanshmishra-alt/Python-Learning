# ============================================================
# PRACTICE PROBLEM 2 — FILTER EVEN NUMBERS
# ============================================================

# Problem:
# Given a list of numbers, create a new list containing
# ONLY the even numbers using LIST COMPREHENSION.
#
# You must NOT use a normal for loop.
#
# Input:
# numbers = [3, 8, 11, 14, 17, 20, 23, 26]
#
# Expected Output:
# [8, 14, 20, 26]
#
# Hint:
# An even number gives remainder 0 when divided by 2.
#
# Use:
# [expression for item in collection if condition]
#
# Write your solution below:
# ============================================================
numbers = [3, 8, 11, 14, 17, 20, 23, 26]
result = [x for x in numbers if x % 2 == 0]
print(result)