# Write a Python program that takes a number from the user
# and checks whether it is a prime number or not.
#
# Example:
# Input: 7
# Output: Prime

n = int(input("Enter a number: "))
def is_prime(n):
    if n <=1:
        return False
    i = 2
    while n > i:
        if n % i == 0:
            return False
        i = i + 1
        
    return True

    
print(is_prime(n))