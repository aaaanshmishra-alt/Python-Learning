# ============================================================
# PRACTICE PROBLEM 5 — FILTER WORDS BY LENGTH
# ============================================================

# Problem:
# Given a list of words, create a dictionary containing
# ONLY the words whose length is greater than 4.
#
# Each word should be the KEY.
# Its length should be the VALUE.
#
# Input:
# words = ["cat", "apple", "dog", "banana", "sun", "elephant"]
#
# Expected Output:
# {
#     "apple": 5,
#     "banana": 6,
#     "elephant": 8
# }
#
# Hint:
# Use len(word) > 4 as your filtering condition.
#
# Structure:
# {key: value for item in collection if condition}
#
# Write your solution below:
# ============================================================

words = ["cat", "apple", "dog", "banana", "sun", "elephant"]
result = {x : len(x) for x in words if len(x) > 4 }
print(result)