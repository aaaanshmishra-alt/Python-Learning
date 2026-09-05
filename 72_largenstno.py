#Write a function:find_largest(numbers)
#takes a list of numbers as a parameter.
#returns the largest number in the list.find_largest([4, 8, 2, 15, 6]) should return 15

def find_largest(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number
    return largest
print(find_largest([12, 15, 16, 18]))