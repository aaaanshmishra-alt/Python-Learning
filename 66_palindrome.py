#Problem Statement
#Write a function named:is_palindrome(n)
#that:
#takes one number as a parameter.
#returns True if the number is a palindrome.
#returns False if the number is not a palindrome

def is_palindrome(n):
    original = n
    reverse = 0

    while n > 0:
        last_digit = n % 10
        reverse = reverse * 10 + last_digit
        n = n // 10

    if original == reverse:
        return True
    else:
        return False

print(is_palindrome(134))

