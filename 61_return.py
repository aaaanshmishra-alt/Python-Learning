#Problem
#Write a function named is_even(n) that:
#* takes one number as a parameter.
#* returns True if the number is even.
#* returns False if the number is odd.
#* Print the returned value.

def even(n):
    if n % 2 == 0:
        return True
    else:
        return False
print(even(6))
