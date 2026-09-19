#waf to add digits of number
#waf to add square of digits of the number
#waf to compute wheather the number is armstrong or not


def is_armstrong(n):
    original = n
    total = 0

    temp = n
    count = 0
    while temp > 0:
        count = count + 1
        temp = temp // 10

    while n > 0:
        last_digit = n % 10
        total = total + last_digit **count
        n = n // 10

    if original == total:
        return True
    else:
        return False
print(is_armstrong(153))


