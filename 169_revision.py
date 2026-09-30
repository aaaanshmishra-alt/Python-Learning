# Write a Python program that takes a number from the user
# and prints:
# "Positive" if the number is greater than 0
# "Negative" if the number is less than 0
# "Zero" if the number is equal to 0

a = int(input("Enter a number: "))
if a > 0:
    print("Positive")
elif a == 0:
    print("zero")
else:
    print("Negative")
    