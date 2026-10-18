# Problem Statement:
# Write a Python program that takes a list of integers
# and returns a new list containing only the numbers
# that are divisible by both 3 and 5.
#
# Example:
# Input: 10 15 20 30 45 22 60
# Output: [15, 30, 45, 60]
#
# Requirements:
# 1. Create a function named divisible_by_both().
# 2. Pass the list as an argument.
# 3. Create and return a new list.
# 4. Do not modify the original list.

def divisible_by_both(numbers):
    result = []

    for num in numbers:
        if num % 3 == 0 and num % 5 == 0:
            result.append(num)

    return result


numbers = list(map(int, input("Enter numbers: ").split()))

answer = divisible_by_both(numbers)

print("Numbers divisible by both 3 and 5:", answer)