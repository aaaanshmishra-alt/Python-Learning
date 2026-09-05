#Write a function named factorial(n) that:
#* takes one number as a parameter.
#* returns the factorial of that number.

def factorial(n):
    result = 1

    while n > 0:
        result = result * n
        n = n - 1

    return result
print(factorial(8))