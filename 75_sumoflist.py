#Problem: Find the Sum of a List
#Write a function:sum_list(numbers)
#takes a list of numbers as a parameter.
#adds all the numbers in the list.
#returns the total sum.

def sum_list(numbers):
    total = 0

    for number in numbers:
        total = total + number
    return total
print(sum_list([1, 2, 3, 4, 5]))