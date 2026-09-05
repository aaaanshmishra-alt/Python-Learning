# Problem 11: Remove Vowels
#
# Write a function:
# remove_vowels(text)
#
# - takes a string.
# - removes all vowels from the string.
# - returns the new string.
#
# Example:
# remove_vowels("hello")
# should return "hll"
#
# remove_vowels("programming")
# should return "prgrmmng"
def remove_vowels(text):
    result = " "
    for character in text:
        if character.lower() not in "aeiou":
            result = result + character
    return result
print(remove_vowels("hello"))
