# Problem 7: Count Digits
#
# Write a function:
# count_digits(text)
#
# - takes a string.
# - counts how many characters in the string are digits.
# - returns the count.
#
# Example:
# count_digits("Ansh123")
# should return 3
#
# count_digits("Python2026")
# should return 4
def count_digits(text):
    count = 0
    for character in text:
        if character.isdigit():
            count = count + 1

    return count
print( count_digits("Python2026"))