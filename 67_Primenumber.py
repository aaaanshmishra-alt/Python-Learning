#Write a function named:is_prime(n)
#takes one number as a parameter.
# returns True if the number is prime.
# returns False if the number is not prime.

def is_prime(n):
    i = 2
    if n <= 1:
        return False

    while n > i:
        if n % i == 0:
            return False
        i = i + 1

    return True
print(is_prime(7))
