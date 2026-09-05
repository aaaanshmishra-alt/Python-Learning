#Take the input from the user and then print the largest digit of that number

n = int(input("Enter a number: "))
largest = 0

while n > 0:
    last_digit = n % 10
    if largest < last_digit:
        largest = last_digit

    n = n // 10
print(largest)