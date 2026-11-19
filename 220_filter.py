# QUESTION 10: Filter Words with Multiple Requirements
#
# You are given a list of words.
#
# Your task:
# 1. Use filter() and lambda.
# 2. Keep words that:
#       - Have more than 4 characters
#       - AND end with the letter "n"
# 3. Store the result in a new list.
# 4. Print the final list.
#
# Input:
# words = ["Python", "lion", "elephant", "sun", "dragon", "cat", "moon"]
#
# Expected Output:
# ["Python", "elephant", "dragon"]

words = ["Python", "lion", "elephant", "sun", "dragon", "cat", "moon"]
result = filter(lambda n : len(n) > 4 and n.endswith("n"), words)
print(list(result))