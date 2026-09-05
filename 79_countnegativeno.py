#Write a function:count_negative(numbers)
# takes a list of numbers as a parameter
# counts how many numbers are lesser than 0
# returns the count

def count_negative(numbers):
    count = 0

    for number in numbers:
        if number < 0:
            count = count + 1
    return count
print(count_negative([-1, 3, -4]))
           