#Armstrong Number
#Problem Statement
#Write a function:is_armstrong(n)
#takes one number as a parameter.
# returns True if the number is an Armstrong number.
#turns False otherwise.

def is_armstrong(n):
    original = n
    total = 0

    while n > 0:
        last_digit = n % 10
        total = total + last_digit ** 3
        n = n // 10
    if original == total:
        return True
    else:
        return False

print(is_armstrong(370))
