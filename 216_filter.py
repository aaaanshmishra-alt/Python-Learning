# QUESTION 6: Filter Using OR
#
# You are given a list of integers.
#
# Your task:
# 1. Use filter() and lambda.
# 2. Keep numbers that satisfy AT LEAST ONE condition:
#       - Less than 10
#       - Divisible by 3
# 3. Store the result in a new list.
# 4. Print the final list.
#
# Input:
# numbers = [4, 9, 10, 12, 14, 15, 20, 21]
#
# Expected Output:
# [4, 9, 12, 14, 15, 21]

numbers = [4, 9, 10, 12, 14, 15, 20, 21]
result = filter(lambda n : n % 3 == 0 or n < 10, numbers)
print(list(result))