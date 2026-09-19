# ============================================================
# PRACTICE PROBLEM 1 — DICTIONARY COMPREHENSION
# ============================================================

# Problem:
# Given a list of numbers, create a dictionary where:
#
# - Each number is the KEY.
# - The square of that number is the VALUE.
#
# Input:
# numbers = [2, 4, 6, 8]
#
# Expected Output:
# {2: 4, 4: 16, 6: 36, 8: 64}
#
# Hint:
# {key: value for item in collection}
#
# Write your solution below:
# ============================================================

numbers = [2, 4, 6, 8]
result = {number: number * number for number in numbers}
print(result)