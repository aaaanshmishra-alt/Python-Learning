# ============================================================
# PHASE 4 — VARIABLE SCOPE
# PROBLEM: COUNTER USING NONLOCAL
# ============================================================
#
# PROBLEM STATEMENT:
#
# Create a function named counter() that contains a local
# variable named count, initially set to 0.
#
# Inside counter(), define another function named increment().
#
# REQUIREMENTS:
#
# 1. The increment() function must use the nonlocal keyword
#    to access count from the enclosing function.
#
# 2. Each time increment() is called, increase count by 1.
#
# 3. Call increment() three times inside counter().
#
# 4. After the three calls, print count inside counter().
#
# 5. Call counter() once.
#
# EXPECTED OUTPUT:
#
# 3
#
# RULES:
#
# - Do not use the global keyword.
# - Do not hardcode the final value 3.
# - Use nonlocal to modify the enclosing function's count.
#
# ============================================================
# WRITE YOUR CODE BELOW
# ============================================================
def counter():
    count = 0
    def increment():
        nonlocal count 
        count = count + 1
    increment()
    increment()
    increment()
    print(count)
counter()