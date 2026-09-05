# Problem 4: Check If Sets Have Anything in Common
#
# Write a function:
# has_common(first, second)
#
# - takes two Sets.
# - returns True if the Sets have at least one
#   element in common.
# - otherwise returns False.
#
# Example:
# has_common({10, 20, 30}, {30, 40, 50})
# should return True
#
# has_common({10, 20}, {30, 40})
# should return False
def has_common(first, second):
    return  not first.isdisjoint(second)
print(has_common({10, 20, 30}, {30, 40, 50}))