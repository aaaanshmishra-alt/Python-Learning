# QUESTION 2: Filter Numbers Greater Than 50
#
# You are given a list of numbers.
#
# Your task:
# 1. Use filter() and lambda.
# 2. Keep only numbers greater than 50.
# 3. Store the result in a new list.
# 4. Print the final list.
#
# Input:
# numbers = [12, 65, 43, 89, 50, 100, 34, 75]
#
# Expected Output:
# [65, 89, 100, 75]

numbers = [12, 65, 43, 89, 50, 100, 34, 75]
result = filter(lambda n : n > 50, numbers)
print(list(result))