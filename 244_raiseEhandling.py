# ============================================================
# EXCEPTION HANDLING PRACTICE 3
# ============================================================
#
# Create a variable:
# age = -10
#
# Requirements:
#
# 1. Check whether age is less than zero.
#
# 2. If age is negative, manually raise ValueError.
#
# 3. Use the error message:
#    "Age cannot be negative!"
#
# 4. Handle the exception using try and except.
#
# 5. Print the exception message using:
#    print(error)
#
# Expected output:
# Age cannot be negative!
#
# ============================================================
try:
    age = 19
    if age < 0:
        raise  ValueError("Age cannot be negative")
except ValueError as error:
    print(error)


