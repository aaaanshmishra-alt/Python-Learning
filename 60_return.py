#Problem
#Write a function named largest(a, b) that:
#* takes two numbers as parameters.
#* returns the larger number.
#* print the returned value.

def largest(a, b):
    if a > b:
        return a
    else:
        return b
print(largest(29, 23))