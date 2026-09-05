# Problem 10: Count Vowels and Consonants
#
# Write a function:
# count_vowels_consonants(text)
#
# - takes a string.
# - counts how many vowels are present.
# - counts how many consonants are present.
# - ignore spaces, digits, and symbols.
# - returns both counts.
#
# Example:
# count_vowels_consonants("Hello World")
# should return:
# (3, 7)
#
# Example:
# count_vowels_consonants("Python 123")
# should return:
# (1, 5)
def count_vowels_consonant(text):
    vowels = 0
    consonants = 0
    for character in text:
        if character.isalpha():
            if character.lower() in "aeiou":
                vowels = vowels + 1
            else:
                consonants = consonants + 1
    return vowels, consonants
print(count_vowels_consonant("Python 123"))
