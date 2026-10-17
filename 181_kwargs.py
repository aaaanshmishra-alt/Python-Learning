# ============================================================
# PROBLEM: COUNT POSITIVE VALUES USING **KWARGS
# ============================================================
#
# Create a function named count_positive() that accepts any
# number of keyword arguments using **kwargs.
#
# REQUIREMENTS:
# 1. Accept any number of keyword arguments.
# 2. Each keyword argument must have a numerical value.
# 3. Count how many values are greater than zero.
# 4. Ignore zero and negative values.
# 5. Return the final count.
#
# EXAMPLE 1:
# Input:
# count_positive(a=10, b=-5, c=20, d=0, e=-3, f=7)
#
# Output:
# 3
#
# EXPLANATION:
# The positive values are 10, 20 and 7.
# Therefore, the total count of positive values is 3.
#
# EXAMPLE 2:
# Input:
# count_positive(a=-10, b=0, c=-5)
#
# Output:
# 0
#
# HINTS:
# 1. Initialize a variable named count with 0.
# 2. Use a for loop to iterate through kwargs.values().
# 3. Use an if condition to check whether a value is positive.
# 4. Increase count by 1 whenever a positive value is found.
# 5. Return count.
#
# Do not hardcode the input values inside the function.
#
# ============================================================

def count_positive(**kwargs):
    count = 0
    for values in kwargs.values():
        if values > 0:
            count = count + 1
    return count
print(count_positive(a=-10, b=0, c=-5))
