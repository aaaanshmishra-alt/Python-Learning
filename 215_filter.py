# QUESTION 5: Filter Numbers Using Multiple Conditions
#
# You are given a list of integers.
#
# Your task:
# 1. Use filter() and lambda.
# 2. Keep numbers that are BOTH:
#       - Even
#       - Greater than 10
# 3. Store the result in a new list.
# 4. Print the final list.
#
# Input:
# numbers = [4, 12, 15, 18, 20, 25, 30, 8, 42]
#
# Expected Output:
# [12, 18, 20, 30, 42]

numbers = [4, 12, 15, 18, 20, 25, 30, 8, 42]
result = filter(lambda n : n % 2 == 0 and n > 10, numbers)
print(list(result))