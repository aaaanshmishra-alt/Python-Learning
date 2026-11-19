# QUESTION 1: Filter Even Numbers using filter()
#
# You are given a list of integers.
#
# Your task:
# 1. Use filter() and lambda.
# 2. Select only the even numbers.
# 3. Store the result in a new list.
# 4. Print the final list.
#
# Input:
# numbers = [12, 7, 18, 23, 40, 35, 50, 9]
#
# Expected Output:
# [12, 18, 40, 50]
#
# Hint:
# An even number is divisible by 2.

numbers = [12, 7, 18, 23, 40, 35, 50, 9]
result = filter(lambda n : n % 2 == 0, numbers)
print(list(result))