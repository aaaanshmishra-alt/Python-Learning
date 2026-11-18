# QUESTION 5: Calculate the Square of Numbers
#
# You are given a list of numbers stored as strings.
#
# Your task:
# 1. Convert each string into an integer.
# 2. Calculate its square using map().
# 3. Store the results in a new list.
# 4. Print the final list.
#
# Input:
# numbers = ["2", "4", "6", "8", "10"]
#
# Expected Output:
# [4, 16, 36, 64, 100]
#
# Hint:
# You can use lambda and int() together.
numbers = ["2", "4", "6", "8", "10"]
square = map(lambda n : int(n) * int(n), numbers)
print(list(square))