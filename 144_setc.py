# ============================================================
# PRACTICE PROBLEM 2 — FILTER EVEN NUMBERS
# ============================================================

# Problem:
# Given a list of numbers, create a SET containing only
# the EVEN numbers.
#
# Input:
# numbers = [1, 2, 2, 3, 4, 5, 6, 6, 7, 8]
#
# Expected Output:
# {2, 4, 6, 8}
#
# Hint:
# Use:
# {expression for item in collection if condition}
#
# Write your solution below:
# ============================================================

numbers = [1, 2, 2, 3, 4, 5, 6, 6, 7, 8]
result = {x for x in numbers if x % 2 == 0 }
print(result)