# Question: Find the Largest Digit
#Problem Statement
#Write a Python program that:
#1. Takes an integer input from the user.
#2. Finds the largest digit in that number.
#3. Prints the largest digit.

n = int(input("Enter a number: "))
largest = 0
while n > 0:
    last_digit = n % 10
    if largest < last_digit:
        largest = last_digit
    
    n = n // 10
print(largest)