# Problem 1: Count a Value in a Tuple
#
# Write a function:
# count_value(numbers, target)
#
# - takes a tuple of numbers and a target number as parameters.
# - returns how many times target appears in the tuple.
#
# Example:
# count_value((10, 20, 10, 30, 10), 10)
# should return 3

def count_value(numbers, target):
    count = 0

    for number in numbers:
        if target == number:
            count = count + 1
    return count
print(count_value((10, 20, 10, 30, 10), 10))