# Problem : Count Zeros
# Write a function:
# count_zeros(numbers)
# - takes a list of numbers as a parameter.
# - counts how many elements are exactly 0.
# - returns the count.
# Example:
# count_zeros([0, 5, 0, -2, 8, 0])
# should return 3

def count_zeros(numbers):
    count = 0

    for number in numbers:
        if number == 0:
            count = count + 1
    return count
print(count_zeros([1,2,3,0,5,90,0]))