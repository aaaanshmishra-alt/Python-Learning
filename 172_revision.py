# Write a Python program that takes a number from the user
# and calculates its factorial using a function.
#
# Example:
# Input: 5
# Output: 120

n = int(input("Enter a number: "))
def factorial(n):
    result = 1

    for i in range(1 , n + 1):
        result = result * i
    return result
print(factorial(n))