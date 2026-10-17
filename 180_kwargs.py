# ============================================================
# PROBLEM: SUM OF POSITIVE VALUES USING **KWARGS
# ============================================================
#
# Create a function named sum_positive() that accepts any
# number of keyword arguments using **kwargs.
#
# Requirements:
# 1. Accept numerical keyword arguments.
# 2. Add only positive values to the total.
# 3. Ignore zero and negative values.
# 4. Return the final total.
#
# Example:
# Input:
# sum_positive(a=10, b=-5, c=20, d=0, e=-3)
#
# Output:
# 30
#
# Explanation:
# 10 + 20 = 30
# -5, 0 and -3 are ignored.
#
# ============================================================
def sum_positive(**kwargs):
    sum = 0
    for values in kwargs.values():
        if values > 0:
            sum = sum + values
    return sum
print(sum_positive(a=10, b=-5, c=20, d=0, e=-3))
