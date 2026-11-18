# QUESTION 4: Type Conversion using map()
#
# You are given a list of numbers stored as strings.
#
# Your task:
# 1. Use map() to convert every string into an integer.
# 2. Store the converted values in a new list.
# 3. Print the final list.
#
# Input:
# numbers = ["10", "25", "40", "55", "100"]
#
# Expected Output:
# [10, 25, 40, 55, 100]
#
# Hint:
# Python has a built-in function called int().

numbers = ["10", "25", "40", "55", "100"]
integer = map(lambda n : int(n), numbers)
print(list(integer))