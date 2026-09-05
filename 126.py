#waf to print the last two digit of a number
def lasttwo_digit(n):
    digit = 0
    count = 0
    while n > 0 :
        last_digit = n % 10
        digit = digit * 10 + last_digit
        n = n // 10
        count = count + 1
        if count == 2:
            break
    return digit
print(lasttwo_digit(12345))
    
        

    

