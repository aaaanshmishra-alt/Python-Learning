# ============================================================
# PROBLEM: FIND THE LARGEST VALUE USING **KWARGS
# ============================================================
#
# Create a function named find_largest() that accepts any
# number of keyword arguments using **kwargs.
#
# REQUIREMENTS:
# 1. Accept any number of keyword arguments.
# 2. Each keyword argument must have a numerical value.
# 3. Find the largest value among all the given values.
# 4. Return the largest value.
#
# EXAMPLE 1:
# Input:
# find_largest(a=10, b=25, c=7, d=40, e=15)
#
# Output:
# 40
#
# EXAMPLE 2:
# Input:
# find_largest(x=-10, y=-3, z=-20)
#
# Output:
# -3
#
# EXAMPLE 3:
# Input:
# find_largest(first=100)
#
# Output:
# 100
#
# HINTS:
# 1. Initialize a variable to store the largest value.
# 2. Iterate through kwargs.values().
# 3. Compare each value with your current largest value.
# 4. If the current value is larger, update your variable.
# 5. Return the largest value.
#
# Do not hardcode the input values inside the function.
#
# ============================================================

def find_largest(**kwargs):
    largest = next(iter(kwargs.values()))
    for values in kwargs.values():
        if values > largest:
            largest = values
    return largest
print(find_largest(first=100))