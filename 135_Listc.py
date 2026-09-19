# ============================================================
# PRACTICE PROBLEM 8 — FINAL LIST COMPREHENSION CHALLENGE
# ============================================================

# Problem:
# Given a list of numbers, create a new list containing
# ONLY the positive numbers, but store their SQUARES.
#
# Input:
# numbers = [-3, 2, -1, 4, 5, -6, 7]
#
# Expected Output:
# [4, 16, 25, 49]
#
# Hint:
# You need BOTH:
# 1. A condition to select positive numbers.
# 2. An expression to square them.
#
# Write your solution below:
# ============================================================

numbers = [-3, 2, -1, 4, 5, -6, 7]
result = [x * x for x in numbers if x > 0]
print(result)
