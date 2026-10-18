# ============================================================
# PHASE 4 — VARIABLE SCOPE
# PROBLEM 2: BANK ACCOUNT WITHDRAWAL
# ============================================================
#
# PROBLEM STATEMENT:
#
# Create a global variable named balance with an initial
# value of 2000.
#
# Create a function named withdraw() that performs these
# operations:
#
# 1. Use the global keyword to access the global balance.
#
# 2. Subtract 750 from the existing balance.
#
# 3. Print the updated balance inside the function.
#
# 4. Call withdraw() once.
#
# 5. Print the balance again outside the function.
#
# EXPECTED OUTPUT:
#
# 1250
# 1250
#
# REQUIREMENTS:
#
# - Use a global variable named balance.
# - Define a function named withdraw().
# - Use the global keyword correctly.
# - Do not create a separate local variable for balance.
#
# ============================================================
# WRITE YOUR CODE BELOW
# ============================================================
balance = 2000
def withdraw():
    global balance
    balance = balance - 750
    print(balance)
withdraw()
print(balance)