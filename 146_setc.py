# ============================================================
# PRACTICE PROBLEM 4 — FINAL SET COMPREHENSION CHALLENGE
# ============================================================

# Problem:
# Given a list of words, create a SET containing the
# LENGTH of every word that has more than 3 characters.
#
# Input:
# words = ["cat", "apple", "dog", "banana", "sun", "elephant"]
#
# Expected Output:
# {5, 6, 8}
#
# Hint:
# 1. Filter words whose length is greater than 3.
# 2. Store their lengths in the set.
#
# Use:
# {expression for item in collection if condition}
#
# Write your solution below:
# ============================================================

words = ["cat", "apple", "dog", "banana", "sun", "elephant"]
result = {len(x) for x in words if len(x) > 3}
print(result)