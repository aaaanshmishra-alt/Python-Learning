# Problem 1: Count a Character
#
# Write a function:
# count_character(text, target)
#
# - takes a string and a target character.
# - returns how many times the target appears in the string.
#
# Example:
# count_character("programming", "m")
# should return 2
#
# count_character("banana", "a")
# should return 3

def count_character(text, target):
    count = 0
    for character in text:
        if character == target:
            count = count + 1
    return count
print(count_character("programming", "m"))
