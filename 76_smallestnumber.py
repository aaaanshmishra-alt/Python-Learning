#Write a function:find_smallest(numbers)
#takes a list of numbers as a parameter
#returns the smallest number in the list

def find_smallest(numbers):
    smallest = numbers[0]

    for number in numbers:
        if number< smallest:
            smallest = number
    return smallest
print(find_smallest([12, 13, 14, 15]))