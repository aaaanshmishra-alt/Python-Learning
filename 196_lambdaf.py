# ============================================================
# PHASE 4 — LAMBDA FUNCTIONS
# QUESTION 4: SORT NUMBERS BY LAST DIGIT
# ============================================================
#
# PROBLEM STATEMENT:
#
# You are given the following list:
#
# numbers = [42, 15, 31, 28, 53, 19]
#
# REQUIREMENTS:
#
# 1. Use sorted() to sort the numbers according to their
#    last digit, from smallest to largest.
#
# 2. Use a lambda function with the key parameter.
#
# 3. Store the result in a variable named result.
#
# 4. Print result.
#
# HINT:
#
# The expression n % 10 gives the last digit of a positive
# integer.
#
# EXPECTED OUTPUT:
#
# [31, 42, 53, 15, 28, 19]
#
# RULES:
#
# - Use lambda, not def.
# - Use the modulo operator (%).
# - Do not manually rearrange the numbers.
#
# ============================================================
# WRITE YOUR CODE BELOW
# ============================================================
numbers = [42, 15, 31, 28, 53, 19]
result = sorted(numbers, key=lambda numbers : numbers % 10)
print(result)