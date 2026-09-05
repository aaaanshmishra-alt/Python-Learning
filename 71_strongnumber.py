#Write a function:
#is_strong(n)
#takes one number as a parameter.
#returns True if the number is a Strong Number.
#returns False otherwise.
 
def factorial(n):
    i = 1
    result = 1

    while i <= n:
        result = result * i
        i = i + 1
    return result

def is_strong(n):
    original = n
    total = 0

    while n > 0:
        last_digit = n % 10
        total = total + factorial(last_digit)
        n = n // 10
    if original == total:
        return True
    else:
        return False

print(is_strong(145))

