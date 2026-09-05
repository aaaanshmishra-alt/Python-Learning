# Problem 8: Find the Second Largest Number
#
# Write a function:
# second_largest(numbers)
#
# - takes a list of numbers as a parameter.
# - finds and returns the SECOND LARGEST number.
#
# Example:
# second_largest([10, 5, 8, 20, 15])
# should return 15
#
# Because:
# Largest = 20
# Second largest = 15

def second_largest(numbers):

    if numbers[0] > numbers[1]:
        largest = numbers[0]
        second_largest = numbers[1]
    else:
        largest = numbers[1]
        second_largest = numbers[0]

    for i in range(2, len(numbers)):
        number = numbers[i]

        if number > largest:
            second_largest = largest
            largest = number

        elif number > second_largest:
            second_largest = number

    return second_largest


print(second_largest([10, 5, 8, 20, 15]))