# QUESTION 4: Filter Positive Numbers
#
# You are given a list containing positive numbers, negative numbers and zero.
#
# Your task:
# 1. Use filter() and lambda.
# 2. Keep only numbers greater than 0.
# 3. Store the result in a new list.
# 4. Print the final list.
#
# Input:
# numbers = [-10, 5, 0, -3, 12, -7, 8, 20]
#
# Expected Output:
# [5, 12, 8, 20]

numbers = [-10, 5, 0, -3, 12, -7, 8, 20]
result = filter(lambda n : n > 0, numbers)
print(list(result))