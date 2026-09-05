# Problem 1: Remove Duplicates
#
# Write a function:
# remove_duplicates(numbers)
#
# - takes a list of numbers.
# - returns a Set containing only the unique numbers.
#
# Example:
# remove_duplicates([10, 20, 10, 30, 20, 40])
# should return:
# {10, 20, 30, 40}
def remove_duplicates(numbers):
    return set(numbers)
print(remove_duplicates([10, 20, 10, 30, 20, 40]))