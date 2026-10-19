# ============================================================
# PHASE 4 — LAMBDA FUNCTIONS
# QUESTION 2: EVEN OR ODD
# ============================================================
#
# PROBLEM STATEMENT:
#
# 1. Create a lambda function that accepts one argument, n.
#
# 2. If n is divisible by 2, return the string "Even".
#
# 3. Otherwise, return the string "Odd".
#
# 4. Store the lambda function in a variable named check.
#
# 5. Call check() with the arguments 8, 13, and 0.
#
# 6. Print the result of each call.
#
# EXPECTED OUTPUT:
#
# Even
# Odd
# Even
#
# RULES:
#
# - Use lambda, not def.
# - Use the modulo operator (%) to check divisibility.
# - Use a conditional expression (if/else).
# - Do not hardcode the answers.
#
# ============================================================
# WRITE YOUR CODE BELOW
# ============================================================
check = lambda n : "even" if n % 2 == 0 else "Odd"
print(check(8))
print(check(13))
print(check(0))