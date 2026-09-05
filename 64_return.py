#Problem is to create a function first and then it shooould return the number of digit in the number 

def countdigit(n):
    count = 0

    while n > 0:
        count = count + 1
        n = n // 10
    return count
print(countdigit(234))
