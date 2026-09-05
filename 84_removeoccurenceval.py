# Problem 7: Remove All Occurrences of a Value
#
# Write a function:
# remove_all(numbers, target)
#
# - takes a list of numbers and a target number as parameters.
# - removes every occurrence of target from the list.
# - returns the resulting list.
#
# Example:
# remove_all([2, 5, 2, 8, 2, 10], 2)
# should return [5, 8, 10]

def remove_all(numbers, target):
    result = []

    for number in numbers:
        if number != target:
            result.append(number)

    return result
print(remove_all([2, 5, 2, 8, 2, 10], 2))