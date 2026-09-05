#Write a function:count_even(numbers)
#takes a list of numbers as a parameter.
#counts how many even numbers are present in the list.
#returns the count.

def count_even(numbers):
    count = 0

    for number in numbers:
        if number % 2 == 0:
            count = count + 1
    return count
print(count_even([10, 23, 24, 22]))