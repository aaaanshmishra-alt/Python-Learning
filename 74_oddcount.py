#Write a function count_odd(numbers) that returns the number of odd values in a list.

def count_odd(numbers):
    count = 0

    for number in numbers:
        if number % 2 == 1:
            count = count + 1
    return count
print(count_odd([12, 13, 14, 15]))