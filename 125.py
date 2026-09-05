def add_digit(n):
    sum = 0

    while n > 0:
        last_digit = n % 10
        sum = sum + last_digit**2
        n = n // 10
    return sum
print(add_digit(22))
