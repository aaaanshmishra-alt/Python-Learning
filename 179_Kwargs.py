# ============================================================
# PROBLEM STATEMENT: CALCULATE TOTAL USING **KWARGS
# ============================================================
#
# Create a function named calculate_total() that accepts any
# number of keyword arguments using **kwargs.
# Requirements:
# 1. Accept any number of keyword arguments.
# 2. Each keyword argument must have a numerical value.
# 3. Calculate the sum of all the values passed to the function.
# 4. Print the final total.
#
# Example 1:
# Input: calculate_total(a=10, b=20, c=30)
# Output: 60
#
# Example 2:
# Input: calculate_total(x=5, y=15, z=25, w=35)
# Output: 80
#
# Example 3:
# Input: calculate_total(first=100, second=200)
# Output: 300
#
# Instructions:
# - Use **kwargs to accept the keyword arguments.
# - Use a variable to store the running total.
# - Use a loop to iterate through the values.
# - Add each value to the running total.
# - Print the final total.
# - Do not hardcode the numbers inside the function.
#
# ============================================================

def calculate_total(**kwargs):
    sum = 0
    for values in kwargs.values():
        sum = sum + values
    return sum
print(calculate_total(first=100, second=200))
        

