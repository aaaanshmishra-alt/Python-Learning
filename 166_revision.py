# MODULE 1 — QUESTION 3
#
# Write a Python program that:
#
# 1. Accepts two numbers from the user.
# 2. Displays their:
#    - Addition
#    - Subtraction
#    - Multiplication
#    - Division
#    - Floor Division
#    - Remainder
#
# Use appropriate type conversion for the input.
#
# Write the complete program below.

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

addition = a + b
Subtraction = a - b
Multiplication = a * b
Division = a / b
Floordivision = a // b
Remainder = a % b

print(f"The sum {addition} and the Subtraction {Subtraction} the Multiplication {Multiplication} the division {Division} the Floordivision {Floordivision} and the remainder {Remainder}")