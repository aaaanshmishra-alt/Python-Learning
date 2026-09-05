# PROBLEM 
# Write a function named reverse_number(n) that returns the reverse of a number.

def reversenumber(n):
    reverse = 0 
    while n > 0:
        lastdigit = n % 10
        reverse = reverse * 10 + lastdigit
        n = n // 10
    return reverse
print(reversenumber(5489))

