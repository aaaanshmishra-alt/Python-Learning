# ==========================================
# PRACTICE: CUSTOM EXCEPTION
# ==========================================

# Create a custom exception named InsufficientBalanceError.
#
# Create a variable:
# balance = 500
#
# Create another variable:
# withdrawal = 800
#
# Inside a try block:
# 1. Check whether withdrawal is greater than balance.
# 2. If it is, raise InsufficientBalanceError with the message:
#    "Insufficient balance!"
# 3. Otherwise, print "Withdrawal successful"
#
# Handle InsufficientBalanceError using except.
# Print the error message using 'as error'.
#
# Finally, print "Transaction completed".
#
# Expected output:
# Insufficient balance!
# Transaction completed


class InsufficientclientBalanceError(Exception) :
    pass

balance = 500
withdrawl = 800

try:
    if withdrawl > balance:
        raise InsufficientclientBalanceError("Insufficient Balance")

    print("Balance left after transaction : " , balance - withdrawl)

except InsufficientclientBalanceError as error:
    print(error)

finally:
    print("Transaction completed")

