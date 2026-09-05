#Problem
#Write a function named sum_to_n(n) that:
#* takes one number as a parameter.
#* returns the sum of all numbers from 1 to n.
def sum(n):
    total = 0

    while n > 0:
        total = total + n
        n = n -1

    return total
print(sum(5))


