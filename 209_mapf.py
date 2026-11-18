# QUESTION 7: Calculate Word Lengths using map()
#
# You are given a list of words.
#
# Your task:
# 1. Use map() and lambda.
# 2. Find the length of every word.
# 3. Store the lengths in a new list.
# 4. Print the final list.
#
# Input:
# words = ["Python", "Programming", "AI", "Developer", "Code"]
#
# Expected Output:
# [6, 11, 2, 9, 4]
#
# Hint:
# Use the built-in len() function.

words = ["Python", "Programming", "AI", "Developer", "Code"]
length = map(lambda n : len(n), words)
print(list(length))
print(list(length))