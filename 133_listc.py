# ============================================================
# PRACTICE PROBLEM 6 — POSITIVE / NEGATIVE
# ============================================================

# Problem:
# Given a list of integers, create a new list where:
#
# - If the number is POSITIVE → put "Positive"
# - If the number is NEGATIVE → put "Negative"
# - If the number is 0 → put "Zero"
#
# You must use LIST COMPREHENSION.
#
# Input:
# numbers = [5, -2, 0, 8, -7, 3, 0, -1]
#
# Expected Output:
# ["Positive", "Negative", "Zero", "Positive",
#  "Negative", "Positive", "Zero", "Negative"]
#
# Hint:
# This time you have THREE possible outcomes.
#
# You can use:
# "Positive" if condition else "Negative" if condition else "Zero"
#
# Write your solution below:
# ============================================================

numbers = [5, -2, 0, 8, -7, 3, 0, -1]
result = ["Positive" if x > 0 else "Negative" if x < 0 else "Zero" for x in numbers]
print(result)