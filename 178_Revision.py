# Problem Statement:
# Write a Python program that takes a list of integers
# and returns the sum of all the numbers that occur only once.
#
# Example:
# Input: 10 20 10 30 40 20 50
# Output: 120
#
# Explanation:
# Numbers occurring only once are 30, 40, and 50.
# Their sum is 30 + 40 + 50 = 120.
#
# Requirements:
# 1. Create a function named sum_unique().
# 2. Pass the list as an argument.
# 3. Find the numbers that appear exactly once.
# 4. Return their sum.
#
# Your Task:
# Write the complete program below.


def sum_unique(numbers):
    # Write your logic here
    pass


numbers = list(map(int, input("Enter numbers: ").split()))

result = sum_unique(numbers)

print("Sum of unique numbers:", result)
