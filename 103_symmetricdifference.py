# Problem 5: Find Non-Common Elements
#
# Write a function:
# non_common(first, second)
#
# - takes two Sets.
# - returns elements that are present in either Set
#   but NOT in both.
#
# Example:
# non_common({10, 20, 30}, {30, 40, 50})
# should return:
# {10, 20, 40, 50}
def non_common(first, second):
    return first.symmetric_difference(second)
print(non_common({10, 20, 30}, {30, 40, 50}))
