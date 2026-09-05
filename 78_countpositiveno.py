#Write a function:count_positive(numbers)
# takes a list of numbers as a parameter
# counts how many numbers are greater than 0
# returns the count

def count_positive(numbers):
    count = 0

    for number in numbers:
        if number > 0:
            count = count + 1
    return count
print(count_positive([2, 4, 5, 6]))
    