# Write a Python program that:
# 1. Takes a number from the user.
# 2. Prints its square.
# 3. Prints its cube.
# 4. Prints whether the number is positive, negative, or zero.
# 5. Prints whether the number is even or odd.

n = int(input("Enter a number: "))
def square(n):
    print(n * n)
def cube(n):
    print(n ** 3)
if n > 0:
    print("The number is positive")
elif n == 0:
    print("The number is zero")
elif n < 0:
    print("The number is negative")
if n % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
square(n)
cube(n)