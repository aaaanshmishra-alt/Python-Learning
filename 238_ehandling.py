# ============================================================
# EXCEPTION HANDLING PRACTICE 1
# ============================================================
#
# 1. Create two variables:
#    num1 = 100
#    num2 = 0
#
# 2. Inside a try block, divide num1 by num2.
#
# 3. Print the result if division is successful.
#
# 4. Handle ZeroDivisionError using an except block.
#
# 5. Print "Execution completed" outside the
#    try-except structure.
#
# Expected output:
#
# Cannot divide by zero!
# Execution completed
#
# ============================================================

try:

    num1 = 100
    num2 = 0

    result = num1 / num2
    print(result)

except ZeroDivisionError:
    print("This program cannot be executed")
print("Execution completed")