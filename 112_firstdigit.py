# Problem 8: Find First Digit
#
# Write a function:
# first_digit(text)
#
# - takes a string.
# - finds the FIRST digit in the string.
# - returns that digit.
# - if there is no digit, return -1.
#
# Example:
# first_digit("Ansh123")
# should return "1"
#
# first_digit("Python2026")
# should return "2"
#
# first_digit("Hello")
# should return -1
def first_digit(text):
    for character in text:
        if character.isdigit():
         return character
    return -1
print(first_digit("Hello"))
