# Problem 2: Find the First Occurrence
#
# Write a function:
# find_first(numbers, target)
#
# - takes a tuple of numbers and a target number as parameters.
# - returns the index of the FIRST occurrence of target.
# - if target is not present, return -1.
#
# Example:
# find_first((10, 20, 30, 20, 40), 20)
# should return 1
#
# find_first((10, 20, 30), 50)
# should return -1

def find_first(numbers, target):
    try:
        return numbers.index(target)
    except ValueError:
        return -1

print(find_first((10, 20, 30, 20, 40), 20))
