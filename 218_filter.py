# QUESTION 8: Filter Palindrome Words
#
# A palindrome is a word that reads the same forward and backward.
# For example: "madam", "level", "radar".
#
# You are given a list of words.
#
# Your task:
# 1. Use filter() and lambda.
# 2. Keep only words that are palindromes.
# 3. Store the result in a new list.
# 4. Print the final list.
#
# Input:
# words = ["madam", "hello", "level", "python", "radar", "world"]
#
# Expected Output:
# ["madam", "level", "radar"]
#
# Hint:
# You can reverse a string using slicing: word[::-1]

words = ["madam", "hello", "level", "python", "radar", "world"]
result = filter(lambda n: n == n[::-1], words)
print(list(result))