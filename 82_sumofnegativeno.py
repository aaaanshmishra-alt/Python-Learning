# Problem 5: Sum of Negative Numbers
# Write a function:
# sum_negative(numbers)
# - takes a list of numbers as a parameter.
# - adds only the numbers that are less than 0.
# - returns the total sum.
# Example:
# sum_negative([5, -2, 8, -7, -3])
# should return -12
# Because:
# -2 + (-7) + (-3) = -12

def sum_negative(numbers):
    total = 0

    for number in numbers:
        if number < 0:
            total = total + number
    return total
print(sum_negative([-1,-2,-3,-4,-5]))