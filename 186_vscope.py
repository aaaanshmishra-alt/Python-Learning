# ============================================================
# PHASE 4 — VARIABLE SCOPE
# PROBLEM 1: BANK ACCOUNT BALANCE
# ============================================================
#
# PROBLEM STATEMENT:
#
# Create a global variable named balance with an initial
# value of 1000.
#
# Create a function named deposit() that performs the
# following operations:
#
# 1. Use the global keyword to access the global variable.
#
# 2. Add 500 to the existing balance.
#
# 3. Print the updated balance inside the function.
#
# 4. Call the deposit() function once.
#
# 5. After calling the function, print the balance outside
#    the function.
#
# EXPECTED OUTPUT:
#
# 1500
# 1500
#
# REQUIREMENTS:
#
# - Use a global variable named balance.
# - Define a function named deposit().
# - Use the global keyword correctly.
# - Do not create a separate local variable for balance.
#
# ============================================================
# WRITE YOUR CODE BELOW
# ============================================================
balance = 1000
def deposit():
    global balance
    balance = balance + 500
    print(balance)
deposit()
print(balance)