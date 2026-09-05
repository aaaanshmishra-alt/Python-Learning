# Problem 15: First Non-Repeating Character
#
# Write a function:
# first_non_repeating(text)
#
# - takes a string.
# - finds the first character that appears exactly once.
# - returns that character.
# - if every character repeats, return -1.
#
# Example:
# first_non_repeating("aabbcdd")
# should return "c"
#
# first_non_repeating("aabb")
# should return -1
def first_non_repeating(text):
    for character in text:
        if text.count(character) == 1:
            return character

    return -1
print(first_non_repeating("aabbcdd"))