# Problem 3: Find Elements Only in First Set
#
# Write a function:
# only_first(first, second)
#
# - takes two Sets.
# - returns the elements that are present in
#   the FIRST Set but NOT in the second Set.
#
# Example:
# only_first({10, 20, 30}, {20, 30, 40})
# should return:
# {10}
def only_first(first, second):
    return first.difference(second)
print(only_first({10, 20, 30}, {20, 30, 40}))