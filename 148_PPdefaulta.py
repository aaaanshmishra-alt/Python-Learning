# ============================================================
# PRACTICE PROBLEM 1 — DEFAULT ARGUMENT
# ============================================================

# Problem:
# Create a function called `calculate_power`.
#
# The function should take:
# - number
# - exponent, with a DEFAULT value of 2
#
# The function should return number raised to the exponent.
#
# Examples:
#
# calculate_power(5)
# → 25
#
# calculate_power(5, 3)
# → 125
#
# Hint:
# Define the function like:
#
# def function_name(parameter, parameter=default_value):
#
# Write your solution below:
# ============================================================
def calculate_power(number , exponent = 2):
    return number ** exponent
print(calculate_power(5))
print(calculate_power(5, 3))
