# QUESTION 7: Filter Words Starting with "A"
#
# You are given a list of words.
#
# Your task:
# 1. Use filter() and lambda.
# 2. Keep only words that start with the letter "A".
# 3. Store the result in a new list.
# 4. Print the final list.
#
# Input:
# words = ["Apple", "Banana", "Avocado", "Mango", "Apricot", "Grapes"]
#
# Expected Output:
# ["Apple", "Avocado", "Apricot"]
#
# Hint:
# Use the string method startswith().

words = ["Apple", "Banana", "Avocado", "Mango", "Apricot", "Grapes"]
result = filter(lambda n : n.startswith("A"), words)
print(list(result))