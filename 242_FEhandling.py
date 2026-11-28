# ============================================================
# EXCEPTION HANDLING PRACTICE 2
# ============================================================
#
# 1. Create two variables:
#    num1 = 100
#    num2 = 10
#
# 2. Inside try, divide num1 by num2.
#
# 3. Handle ZeroDivisionError using except.
#
# 4. If no exception occurs, use else to print:
#    "Division successful!"
#
# 5. Use finally to print:
#    "Calculation completed!"
#
# 6. Print the division result inside the try block.
#
# ============================================================


try:
    num1 = 100
    num2 = 10

    result = num1/num2
    print(result)

except ZeroDivisionError:
    print("Enter another value")

else:
    print("Divison Successfull")

finally:
    print("Calculation completed")
