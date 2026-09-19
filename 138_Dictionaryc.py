# ============================================================
# PRACTICE PROBLEM 2 — FILTER EVEN NUMBERS
# ============================================================

# Problem:
# Given a list of numbers, create a dictionary containing
# ONLY the EVEN numbers.
#
# Each even number should be the KEY.
# Its square should be the VALUE.
#
# Input:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
#
# Expected Output:
# {2: 4, 4: 16, 6: 36, 8: 64}
#
# Hint:
# Use:
# {key: value for item in collection if condition}
#
# Write your solution below:
# ============================================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = {x : x * x for x in numbers if x % 2 == 0}
print(result)
