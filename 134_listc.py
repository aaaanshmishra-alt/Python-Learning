# ============================================================
# PRACTICE PROBLEM 7 — MIXED DECISION
# ============================================================

# Problem:
# Given a list of numbers, create a new list containing:
#
# - The number itself if it is EVEN
# - The SQUARE of the number if it is ODD
#
# Input:
# numbers = [1, 2, 3, 4, 5, 6]
#
# Expected Output:
# [1, 2, 9, 4, 25, 6]
#
# Hint:
# Every number must produce an output.
# Therefore, you need IF-ELSE, not a filtering if.
#
# Write your solution below:
# ============================================================

numbers = [1, 2, 3, 4, 5, 6]
result = [x if x % 2 == 0 else x * x for x in numbers]
print(result)