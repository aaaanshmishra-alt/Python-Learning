# ============================================================
# PRACTICE PROBLEM 4 — WORD LENGTH DICTIONARY
# ============================================================

# Problem:
# Given a list of words, create a dictionary where:
#
# - Each word is the KEY.
# - The length of the word is the VALUE.
#
# Input:
# words = ["apple", "banana", "cat", "elephant"]
#
# Expected Output:
# {
#     "apple": 5,
#     "banana": 6,
#     "cat": 3,
#     "elephant": 8
# }
#
# Hint:
# Use len() to find the length of each word.
#
# Structure:
# {key: value for item in collection}
#
# Write your solution below:
# ============================================================

words = ["apple", "banana", "cat", "elephant"]
result = {x : len(x) for x in words}
print(result)

