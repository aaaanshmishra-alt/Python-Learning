# Problem : Find the First Even Number
#
# Write a function:
# first_even(numbers)
#
# - takes a list of numbers as a parameter.
# - finds the FIRST even number in the list.
# - returns that number.
# - if there is no even number, return None.
#
# Example:
# first_even([3, 7, 9, 12, 15])
# should return 12
#
# first_even([1, 3, 5, 7])
# should return None

def first_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            return number
    return None
print(first_even([3, 7, 9, 12, 15]))
