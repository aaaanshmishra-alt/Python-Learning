# Problem : Sum of Positive Numbers
#
# Write a function:
# sum_positive(numbers)
#
# - takes a list of numbers as a parameter.
# - adds only the numbers that are greater than 0.
# - returns the total sum.
#
# Example:
# sum_positive([-2, 5, 8, -3, 10])
# should return 23
#
# Because:
# 5 + 8 + 10 = 23

def sum_positive(numbers):
    total = 0

    for number in numbers:
        if number > 0:
            total = total + number
    return total
print(sum_positive([1,2,3,4,5]))