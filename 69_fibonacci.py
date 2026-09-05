#Write a function:
#fibonacci(n)
#where n is the number of terms to print.
def fibonacci(n):
    first = 0 
    second = 1

    for i in range(n):
        print(first)
        third = first + second
        first = second
        second = third

fibonacci(7)

##i this question we dont need to use print(fibonacci(5))becuse the problem is to print the fibonacci number not to return the fibonacci number