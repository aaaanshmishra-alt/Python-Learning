# Problem 2: Count Vowels
#
# Write a function:
# count_vowels(text)
#
# - takes a string.
# - counts how many vowels are present.
# - vowels are: a, e, i, o, u
# - returns the count.
#
# Example:
# count_vowels("hello")
# should return 2
#
# count_vowels("programming")
# should return 3
def count_vowels(text):
    count = 0
    for character in text:
        if character in "aeiou":
            count = count + 1
    return count
print(count_vowels("programming"))

