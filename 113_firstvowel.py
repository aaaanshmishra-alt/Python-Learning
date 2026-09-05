# Problem 9: Find First Vowel
#
# Write a function:
# first_vowel(text)
#
# - takes a string.
# - finds the FIRST vowel.
# - returns that vowel.
# - if there is no vowel, return -1.
#
# Example:
# first_vowel("Ansh")
# should return "A"
#
# first_vowel("Python")
# should return "o"
#
# first_vowel("rhythm")
# should return -1
def first_vowel(text):
    for character in text:
        if character in "aeiou":
            return character
    return -1
print(first_vowel("Python"))