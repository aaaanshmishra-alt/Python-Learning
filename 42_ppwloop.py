#write a program that compute the factorial of the number entered by the user
n = int(input("Enter the number: "))
factorial = 1
i = 1
if n <= 0:
    print("Enter another number which is positive")
while i <= n:
    factorial = factorial * i
    i = i + 1
print(factorial)