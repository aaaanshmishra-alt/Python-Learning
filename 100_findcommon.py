# Problem 2: Find Common Elements
#
# Write a function:
# common_elements(first, second)
#
# - takes two Sets as parameters.
# - returns a Set containing the elements
#   that are present in BOTH Sets.
#
# Example:
# common_elements({10, 20, 30}, {20, 30, 40})
# should return:
# {20, 30}
def common_elements(first, second):
    return first.intersection(second)
print(common_elements({10, 20, 30}, {20, 30, 40}))