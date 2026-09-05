#Write a function:is_perfect(n)
# takes one number as a parameter.
# returns True if the number is a Perfect Number.
# returns False otherwise.

def is_perfect(n):
    total = 0
    i = 1

    while n > i:
        if n % i == 0:
            total = total + i
        i = i + 1

    if n == total:
        return True
    else:
        return False
print(is_perfect(6))

