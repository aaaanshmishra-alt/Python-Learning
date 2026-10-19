# ============================================================
# PHASE 4 — LAMBDA FUNCTIONS
# QUESTION 1: SQUARE OF A NUMBER
# ============================================================
#
# PROBLEM STATEMENT:
#
# 1. Create a lambda function that accepts one argument, n.
#
# 2. The function must return the square of n.
#
# 3. Store the lambda function in a variable named square.
#
# 4. Call square() with the arguments 5 and 9.
#
# 5. Print both results.
#
# EXPECTED OUTPUT:
#
# 25
# 81
#
# RULES:
#
# - Use lambda, not def.
# - Do not hardcode the answers.
# - Use the exponentiation operator (**) to calculate
#   the square.
#
# ============================================================
# WRITE YOUR CODE BELOW
# ============================================================
square = lambda n : n * n

print(square(5))
print(square(9))